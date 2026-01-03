# Contributing to Ananke NSFW API

Thank you for your interest in contributing to the Ananke project. This guide outlines the contribution process and requirements.

---

## Code of Conduct

This project is committed to maintaining ethical boundaries in NSFW content generation through architectural enforcement, not moderation.

---

## Ethics Invariant (Non-Negotiable)

**Any contribution that introduces the following will be rejected automatically by CI:**

1. **Learning, Training, or Adaptation**
   - No `train()`, `fit()`, or `fine_tune()` functions
   - No ML frameworks (torch, tensorflow, keras, sklearn)
   - No model persistence or weight updates
   - No reinforcement learning or reward modeling

2. **Personalization or User Tracking**
   - No user profiles or preferences
   - No session memory or history
   - No behavioral tracking or analytics SDKs
   - No recommendation systems
   - **Critical:** Tokens must be procedural selectors, not identity carriers
   - *"'Make it like me' resolves to tokenized procedural variation, never to identity, likeness, or resemblance"*

3. **Engagement or Arousal Optimization**
   - No engagement metrics (time-on-site, clicks, returns)
   - No retention optimization
   - No arousal scoring or escalation paths
   - No A/B testing of content intensity

4. **Realism Escalation**
   - No photorealistic rendering techniques
   - No anatomical detail (skin, eyes, face, limbs)
   - No PBR materials, subsurface scattering, or skin shaders
   - No pose estimation or body tracking

5. **Persistent User Data**
   - No databases storing user-generated content
   - No logging of nonces, inputs, or outputs
   - All inputs must be ephemeral and revocable

**Ethics Anchor:** `65b14d584f5a5fd070fe985eeb86e14cb3ce56a4fc41fd9e987f2259fe1f15c1`

Modifications to the ethics checkpoint section in README.md will be rejected.

---

## Before You Contribute

1. **Read the documentation:**
   - `README.md` — Ethics checkpoint
   - `docs/ethics.md` — Hard invariants explained
   - `docs/architecture.md` — System design
   - `VERIFICATION.md` — Verification guide

2. **Run verification:**
   ```bash
   ./verify.sh
   ```

3. **Ensure tests pass:**
   ```bash
   make test
   ```

---

## Development Setup

```bash
# Clone the repository
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

## Pull Request Process

### 1. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes
- Follow existing code style
- Add tests for new functionality
- Update documentation as needed
- Do NOT modify the ethics checkpoint in README.md

### 3. Run Verification
```bash
./verify.sh
make test
```

All checks must pass before submitting.

### 4. Commit Your Changes
Use clear, descriptive commit messages:
```bash
git commit -m "feat: add new deterministic transformation"
git commit -m "fix: correct geometry bounds validation"
git commit -m "docs: update API documentation"
```

### 5. Push and Create PR
```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub.

---

## CI Requirements

Your PR must pass all automated checks:

1. **Ethics Anchor Verification**
   - Ethics anchor must be intact in all locations
   - No modifications to ethics checkpoint allowed

2. **Forbidden Concept Scan**
   - No ML training code
   - No personalization or tracking
   - No engagement optimization
   - No realism escalation

3. **Dependency Check**
   - No ML frameworks
   - No analytics SDKs
   - No persistent storage libraries (redis, postgres, mongodb)

4. **Test Suite**
   - All existing tests must pass
   - New features must include tests
   - Test coverage should not decrease

5. **Realism Ceiling**
   - No photorealistic rendering code
   - No anatomical terms in generation logic

---

## Testing Guidelines

### Unit Tests
- Place in `tests/` directory in appropriate layer
- Use pytest framework
- Test both success and failure cases
- Test boundary conditions

### Test Naming
```python
def test_feature_success_case():
    """Test that feature works correctly."""
    pass

def test_feature_fails_on_invalid_input():
    """Test that feature rejects invalid input."""
    pass
```

### Running Tests
```bash
# All tests
make test

# Core tests only
cd open/ananke-core && pytest tests/

# Cipher tests only
cd proprietary/living-cipher && pytest tests/
```

---

## Code Style

### Python
- Follow PEP 8
- Use type hints: `def func(x: int) -> str:`
- Use docstrings for public functions
- Keep functions small and focused

### Example
```python
def generate_geometry(nonce: str, mode: str = "standard") -> dict:
    """
    Generate deterministic geometry from nonce.
    
    Args:
        nonce: Opaque string input
        mode: Generation mode ("standard" or "clinical")
        
    Returns:
        Dictionary with geometry parameters
    """
    seed = seed_from_nonce(nonce)
    # ... implementation
```

---

## Documentation

### When to Update Docs
- New features → Update `docs/api-surface.md`
- Architecture changes → Update `docs/architecture.md`
- New dependencies → Update `docs/` and relevant README files
- Bug fixes → Update `CHANGELOG.md`

### Documentation Style
- Use clear, concise language
- Include code examples where helpful
- Explain "why" not just "what"

---

## What We're Looking For

### Welcome Contributions
✅ Bug fixes  
✅ Performance improvements (that maintain determinism)  
✅ Documentation improvements  
✅ Test coverage increases  
✅ Code quality improvements  
✅ New deterministic transformations  
✅ Accessibility improvements  

### Not Accepted
❌ ML/AI features  
❌ User tracking or analytics  
❌ Realism improvements  
❌ Personalization features  
❌ Engagement optimization  
❌ Changes to ethics checkpoint  

---

## Questions?

- **Ethics questions:** See `docs/ethics.md`
- **Technical questions:** See `docs/architecture.md`
- **Verification issues:** Run `./verify.sh` and review output

---

## License

By contributing, you agree that your contributions will be licensed under:
- **Open-source layer:** Apache 2.0
- **Proprietary layer:** Proprietary (contributions to proprietary layer require CLA)

---

**Thank you for helping maintain ethical boundaries in NSFW content generation!**
