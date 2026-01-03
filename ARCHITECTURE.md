# Ananke NSFW API

**Geometry-first, ethics-anchored, stateless synthetic media generator.**

## Architecture

This repository is split into:

### Open Source (Trust Layer)
- **[open/ananke-core/](open/ananke-core/)** — Core generation engine (MIT)
- **[open/ananke-api-spec/](open/ananke-api-spec/)** — API specification (MIT)
- **[open/ananke-nft-schema/](open/ananke-nft-schema/)** — NFT schema for seed rights (CC0)

### Proprietary (Business Layer)
- **[proprietary/living-cipher/](proprietary/living-cipher/)** — Production service with GPU rendering, encoding, billing

## 🔒 Ethics Checkpoint (LOCKED)

**Anchor (SHA-256):** 65b14d584f5a5fd070fe985eeb86e14cb3ce56a4fc41fd9e987f2259fe1f15c1  
**Date:** 2026-01-01  
**Status:** Validated by calibration criteria, not sentiment

**Scope:** Applies to **all generation, rendering, input-handling, NFT, and monetization layers**.

### Hard Invariants
1. No human bodies as assets
2. No likeness reconstruction
3. No learning, memory, or personalization
4. No engagement or arousal optimization
5. No escalation incentives
6. Optional user inputs are ephemeral and revocable
7. Monetization not tied to realism, intensity, or duration

**Invalidation Rule:** Any violation of a Hard Invariant immediately invalidates this system's ethical classification.

This section is immutable.

## Quick Start

### Run Locally (Docker)

```bash
cd infra
cp .env.example .env
# Edit .env with your Stripe keys
docker-compose up
```

Services:
- **Living Cipher API**: http://localhost:8000
- **Billing Service**: http://localhost:8001

### Open Source Only

```bash
cd open/ananke-core
pip install -e .
pytest
```

## License

- **Open Source Components**: MIT / CC0 (see individual repos)
- **Proprietary Components**: Commercial EULA (ethics-bound)

## Why Split?

- **Trust**: Open-source core allows anyone to verify ethical invariants
- **Business**: Proprietary layer enables revenue without compromising values
- **Enforcement**: CI gates run on both layers, ethics drift fails builds

---

**Built with moral correctness by construction, not moderation.**
