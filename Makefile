.PHONY: help verify test clean install dev prod health ethics cipher-test

help:
	@echo "Ananke NSFW API — Build Automation"
	@echo "==================================="
	@echo ""
	@echo "Targets:"
	@echo "  make verify       — Run complete verification suite"
	@echo "  make test         — Run all unit tests"
	@echo "  make ethics       — Check ethics anchor and invariants"
	@echo "  make cipher-test  — Test Living Cipher determinism"
	@echo "  make install      — Install all dependencies"
	@echo "  make dev          — Start development environment"
	@echo "  make prod         — Start production environment"
	@echo "  make health       — Check service health"
	@echo "  make clean        — Clean temporary files"
	@echo ""

verify:
	@echo "Running complete verification..."
	@./verify.sh

test:
	@echo "Running unit tests..."
	@cd open/ananke-core && python -m pytest tests/ -v
	@cd proprietary/living-cipher && python -m pytest tests/ -v

ethics:
	@echo "Checking ethics anchor..."
	@grep -r "65b14d584f5a5fd070fe985eeb86e14cb3ce56a4fc41fd9e987f2259fe1f15c1" . --include="*.py" --include="*.md" || (echo "❌ Ethics anchor not found" && exit 1)
	@echo "✓ Ethics anchor verified"
	@echo ""
	@echo "Scanning for forbidden concepts..."
	@! grep -rn -E "train\(|fit\(|reinforcement|engagement|arousal" open/ananke-core/ananke_core/ proprietary/living-cipher/app/ 2>/dev/null | grep -v "FORBIDDEN" | grep -v test || (echo "❌ Forbidden concepts detected" && exit 1)
	@echo "✓ No forbidden concepts found"

cipher-test:
	@echo "Testing Living Cipher..."
	@echo "1. Checking if service is running..."
	@curl -f http://localhost:8000/health > /dev/null 2>&1 || (echo "❌ Service not running. Run 'make dev' first." && exit 1)
	@echo "✓ Service is up"
	@echo ""
	@echo "2. Testing determinism..."
	@curl -s -X POST "http://localhost:8000/v1/generate?nonce=test-seed" > /tmp/out1.json
	@curl -s -X POST "http://localhost:8000/v1/generate?nonce=test-seed" > /tmp/out2.json
	@diff /tmp/out1.json /tmp/out2.json && echo "✓ Determinism verified" || (echo "❌ Output not deterministic" && exit 1)
	@echo ""
	@echo "3. Testing video determinism..."
	@curl -s -X POST "http://localhost:8000/v1/generate/video?nonce=vseed&frames=5" > /tmp/v1.json
	@curl -s -X POST "http://localhost:8000/v1/generate/video?nonce=vseed&frames=5" > /tmp/v2.json
	@diff /tmp/v1.json /tmp/v2.json && echo "✓ Video determinism verified" || (echo "❌ Video not deterministic" && exit 1)
	@echo ""
	@echo "✓ All cipher tests passed"

install:
	@echo "Installing dependencies..."
	@pip install -r open/ananke-core/requirements.txt
	@pip install -r proprietary/living-cipher/requirements.txt
	@pip install -r proprietary/living-cipher/billing/requirements.txt
	@echo "✓ Dependencies installed"

dev:
	@echo "Starting development environment..."
	@cd infra && docker-compose up

prod:
	@echo "Starting production environment..."
	@cd infra && docker-compose -f docker-compose.prod.yml up -d

health:
	@echo "Checking service health..."
	@curl -s http://localhost:8000/health | python -m json.tool
	@echo ""
	@curl -s http://localhost:8001/health | python -m json.tool

clean:
	@echo "Cleaning temporary files..."
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@rm -f /tmp/out*.json /tmp/v*.json
	@echo "✓ Cleaned"

attestation:
	@echo "Generating attestation document..."
	@TIMESTAMP=$$(date -u +"%Y-%m-%d %H:%M:%S UTC"); \
	COMMIT=$$(git rev-parse HEAD 2>/dev/null || echo "UNKNOWN"); \
	SHORT_COMMIT=$$(git rev-parse --short HEAD 2>/dev/null || echo "UNKNOWN"); \
	cp docs/ATTESTATION.md docs/ATTESTATION-$${SHORT_COMMIT}.md; \
	sed -i "s/\[AUTO-GENERATED\]/$${TIMESTAMP}/g" docs/ATTESTATION-$${SHORT_COMMIT}.md; \
	sed -i "s/\[AUTO-GENERATED\]/$${COMMIT}/g" docs/ATTESTATION-$${SHORT_COMMIT}.md; \
	echo "✓ Attestation saved to docs/ATTESTATION-$${SHORT_COMMIT}.md"
	@echo ""
	@echo "Running verification to validate attestation claims..."
	@./verify.sh
	@echo ""
	@echo "✅ Attestation document generated and verified"
