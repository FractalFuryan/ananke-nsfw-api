# System Architecture

## Overview

Ananke is a geometry-first, deterministic synthetic media generator with **hard ethical invariants enforced by construction**, not content moderation.

## Architecture Layers

### 1. Open Source Trust Layer

**ananke-core** (MIT License)
- Pure geometry generation
- Deterministic from seed
- No machine learning
- No user data processing
- Publicly auditable

Components:
- `core.py`: Seed-to-geometry transformation
- `video.py`: Procedural motion (phase-based)
- `render.py`: Abstract SVG output

### 2. Proprietary Business Layer

**Living Cipher** (Commercial EULA)
- Production API service
- FFmpeg encoding
- GPU rendering (stylized only)
- Stateless workers
- Feature flags & monitoring

### 3. Optional Billing Layer

**Billing Service** (Isolated)
- Stripe integration
- Webhook verification
- No cross-contamination with generator

## Data Flow

**Token-Based Configuration (Not Identity Personalization):**

User interaction occurs **only via stateless tokens**:
- **Nonce/Seed:** Opaque string that selects procedural variation
- **Mode flags:** `standard`, `clinical` (operational mode selection)
- **Parameters:** Bounded numeric inputs (frames, duration)

**Critical distinction:**
- ✅ **Allowed:** Tokens as procedural selectors (e.g., `seed="my-vibe"`)
- ❌ **Forbidden:** Tokens encoding identity, biometric data, preferences

**Key principle:** *"'Make it like me' resolves to a tokenized procedural variation, never to identity, likeness, or resemblance."*

**Token Properties:**
- Stateless (no memory between requests)
- Non-identifying (cannot encode person, body, face)
- Deterministic (reproducible outputs)
- Ephemeral (processed in-flight, never stored)
- Revocable (no persistent effects)

**Processing Flow:**

```
Nonce (user input)
  ↓
[SHA-256 Hash] → Seed
  ↓
[Logistic Map] → Chaos value
  ↓
[Bounded Parameters] → Geometry
  ↓
[Abstract Renderer] → SVG/Video
  ↓
[Optional Encoding] → MP4
```

**No feedback loops. No learning. No memory.**

## Deployment Architecture

```
┌─────────────────┐
│  Load Balancer  │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
┌───▼───┐ ┌──▼────┐
│Living │ │Living │  (Stateless, horizontal scale)
│Cipher │ │Cipher │
└───┬───┘ └──┬────┘
    │        │
    └────┬───┘
         │
    ┌────▼────┐
    │  Queue  │  (Optional, for batch jobs)
    └────┬────┘
         │
    ┌────▼────┐
    │ Workers │  (Stateless, auto-scale)
    └─────────┘
```

## Security Boundaries

1. **Generator Core**: No external inputs except nonce
2. **API Layer**: Rate limiting (non-behavioral), revocation
3. **Billing**: Isolated, no generator influence
4. **Workers**: Stateless, no cross-job communication

## Ethical Enforcement Points

1. **Core**: Bounded parameters, no realism keys
2. **CI**: Pattern detection for forbidden concepts
3. **Runtime**: Realism guards at renderer boundary
4. **Contract**: EULA binds to ethics anchor

## Scaling Properties

- **Horizontal**: Stateless workers scale infinitely
- **Vertical**: GPU acceleration for rendering
- **Cache**: Deterministic outputs can be cached by nonce
- **CDN**: Static assets (web client) edge-deployable

## Monitoring

- Health checks with ethics verification
- Feature flag status
- Aggregate usage (optional, privacy-preserving)
- **No user tracking**

## Threat Model Coverage

See [threat-model.md](threat-model.md) for complete analysis.
