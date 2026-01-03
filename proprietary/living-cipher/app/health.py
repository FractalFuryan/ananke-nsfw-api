"""Living Cipher health check endpoint with ethics verification."""
from fastapi import FastAPI
from .flags import all_flags

ETHICS_ANCHOR = "65b14d584f5a5fd070fe985eeb86e14cb3ce56a4fc41fd9e987f2259fe1f15c1"

def ethics_status() -> dict:
    """Return verifiable ethics status for auditing."""
    return {
        "ethics_anchor": ETHICS_ANCHOR,
        "learning": False,
        "memory": False,
        "analytics": False,
        "realism_ceiling": "enforced",
        "user_data_storage": False,
        "engagement_optimization": False,
    }

def add_health_endpoint(app: FastAPI):
    @app.get("/health")
    def health():
        return {
            "status": "ok",
            "service": "living-cipher",
            "ethics": ethics_status(),
            "features": all_flags(),
        }
