# Ananke NSFW API — v1.0 Release

**Status:** Production-ready  
**Ethics:** Locked by construction  
**Verification:** Complete  
**Release Date:** 2026-01-03

---

## Overview

This release marks the first stable, audited version of the Ananke NSFW media generation system. All core ethical invariants are enforced architecturally and verified via automated tooling.

**Ethics Anchor:** `65b14d584f5a5fd070fe985eeb86e14cb3ce56a4fc41fd9e987f2259fe1f15c1`

---

## Key Features

### Ethical Guarantees
- ✅ No human bodies, no likeness reconstruction
- ✅ No learning, memory, or personalization
- ✅ No engagement optimization or escalation incentives
- ✅ Deterministic, stateless, non-adaptive architecture

### Technical Capabilities
- Geometry-first procedural generation
- Deterministic video synthesis (FFmpeg)
- Clinical/harm-reduction mode
- Privacy-preserving aggregate monitoring (opt-in only)
- GPU-accelerated rendering (abstract shaders only)
- Stateless queue workers for scaling

### Verification & Compliance
- 19/19 automated tests passing
- Comprehensive verification suite (`./verify.sh`)
- Automated attestation generation (`make attestation`)
- CI/CD ethics gates on every commit
- Complete regulator documentation pack

---

## Installation

```bash
# Clone repository
git clone https://github.com/FractalFuryan/ananke-nsfw-api.git
cd ananke-nsfw-api

# Install dependencies
make install

# Run verification
./verify.sh

# Start development server
make dev
```

---

## Quick Start

```bash
# Check system status
./status.sh

# Run all tests
make test

# Generate attestation
make attestation

# Start production environment
make prod
```

---

## Documentation

For detailed information, see:

- **[VERIFICATION.md](VERIFICATION.md)** — Complete verification guide and test results
- **[ATTESTATION.md](docs/ATTESTATION.md)** — Compliance attestation template
- **[docs/](docs/)** — Regulator documentation pack:
  - `architecture.md` — System design and data flow
  - `ethics.md` — Hard invariants explained
  - `threat-model.md` — Security analysis
  - `invariant-matrix.md` — Compliance checklist
  - `api-surface.md` — API documentation
  - `clinical-mode.md` — Harm reduction guidelines
  - `addiction-monitoring.md` — Privacy implementation

---

## Repository Structure

```
ananke-nsfw-api/
├── open/ananke-core/          # Open-source trust layer
│   ├── ananke_core/           # Deterministic geometry generator
│   └── tests/                 # Core unit tests (5)
├── proprietary/living-cipher/ # Business layer
│   ├── app/                   # FastAPI service + guards
│   ├── billing/               # Stripe integration (isolated)
│   ├── render_gpu/            # GPU renderer stub
│   ├── worker/                # Stateless queue workers
│   ├── web/                   # Web client (abstract preview)
│   └── tests/                 # Cipher tests (14)
├── docs/                      # Regulator documentation
├── .github/workflows/         # CI/CD with ethics gates
├── verify.sh                  # Automated verification script
├── status.sh                  # Quick status check
├── Makefile                   # Build automation (10 targets)
└── VERIFICATION.md            # Verification guide
```

---

## Compliance

This system is designed for:
- ✅ Regulator engagement
- ✅ Public audit
- ✅ Clinical/research use
- ✅ Ethical deployment

All claims are backed by:
- Code (guards, bounds, determinism)
- Tests (19 automated tests)
- CI gates (ethics drift detection)
- Attestation artifacts (timestamped reports)

---

## License

- **Open-source layer:** Apache 2.0 (see `open/ananke-core/LICENSE`)
- **Proprietary layer:** Proprietary (see `proprietary/living-cipher/LICENSE`)

---

## Support

For questions about:
- **Ethics compliance:** See `docs/ethics.md`
- **Technical architecture:** See `docs/architecture.md`
- **Security:** See `docs/threat-model.md`
- **Verification:** Run `./verify.sh`

---

## Version History

- **v1.0.0** (2026-01-03) — Initial production release with complete verification infrastructure

---

**This repository is safe to build, run, and audit.**

Ethics Anchor: `65b14d584f5a5fd070fe985eeb86e14cb3ce56a4fc41fd9e987f2259fe1f15c1`
