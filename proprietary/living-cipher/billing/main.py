import os
import stripe
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI(title="billing", version="0.1")

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY", "")
WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET", "")
PRICE_ID = os.environ.get("STRIPE_PRICE_ID", "")

@app.post("/v1/billing/checkout")
def create_checkout(customer_ref: str):
    """Create Stripe Checkout Session for subscription/payment."""
    if not stripe.api_key or not PRICE_ID:
        raise HTTPException(500, "Stripe not configured")
    
    session = stripe.checkout.Session.create(
        mode="subscription",  # or "payment"
        line_items=[{"price": PRICE_ID, "quantity": 1}],
        success_url=os.environ.get("SUCCESS_URL", "http://localhost:3000/success"),
        cancel_url=os.environ.get("CANCEL_URL", "http://localhost:3000/cancel"),
        client_reference_id=customer_ref,
        metadata={"customer_ref": customer_ref},
    )
    return {"checkout_url": session.url, "session_id": session.id}

@app.post("/v1/billing/webhook")
async def stripe_webhook(request: Request):
    """Handle Stripe webhook events with signature verification."""
    payload = await request.body()
    sig = request.headers.get("stripe-signature")
    if not sig:
        raise HTTPException(400, "Missing Stripe-Signature header")

    try:
        event = stripe.Webhook.construct_event(payload, sig, WEBHOOK_SECRET)
    except Exception as e:
        raise HTTPException(400, f"Invalid webhook signature: {e}")

    # Handle checkout.session.completed
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        customer_ref = session.get("client_reference_id") or session.get("metadata", {}).get("customer_ref")
        
        # TODO: Mark customer_ref as "active" in your database
        # This should be idempotent - webhooks can be retried
        print(f"✅ Subscription activated for: {customer_ref}")

    return JSONResponse({"received": True})

@app.get("/health")
def health():
    return {"status": "ok"}
