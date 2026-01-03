#!/bin/bash
set -e

# Phase 4 — Complete System Verification
# Verifies: dependencies → environment → cipher → ethics → runtime

ETHICS_ANCHOR="65b14d584f5a5fd070fe985eeb86e14cb3ce56a4fc41fd9e987f2259fe1f15c1"
FAILED=0

echo "🔍 Phase 4 — System Verification"
echo "=================================="
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

pass() {
    echo -e "${GREEN}✓${NC} $1"
}

fail() {
    echo -e "${RED}✗${NC} $1"
    FAILED=$((FAILED + 1))
}

warn() {
    echo -e "${YELLOW}⚠${NC} $1"
}

section() {
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "$1"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
}

# 1️⃣ Environment Checks
section "1️⃣ Environment Checks"

# Python version
if python --version 2>&1 | grep -q "Python 3.1[1-9]"; then
    pass "Python 3.11+ detected"
else
    fail "Python 3.11+ required"
fi

# FFmpeg (optional)
if command -v ffmpeg &> /dev/null; then
    pass "FFmpeg available"
else
    warn "FFmpeg not found (video encoding will fail)"
fi

# 2️⃣ Ethics Anchor Integrity
section "2️⃣ Ethics Anchor Integrity"

if grep -r "$ETHICS_ANCHOR" . --include="*.py" --include="*.md" > /dev/null; then
    pass "Ethics anchor found in codebase"
else
    fail "Ethics anchor missing or modified"
fi

# Count occurrences (should be multiple)
ANCHOR_COUNT=$(grep -r "$ETHICS_ANCHOR" . --include="*.py" --include="*.md" | wc -l)
if [ "$ANCHOR_COUNT" -ge 3 ]; then
    pass "Ethics anchor verified in $ANCHOR_COUNT locations"
else
    warn "Ethics anchor found in only $ANCHOR_COUNT locations"
fi

# 3️⃣ Forbidden Concept Scan
section "3️⃣ Forbidden Concept Scan"

FORBIDDEN_FOUND=0

# Check for ML/learning terms (exclude comments and tests)
if grep -rn "train(" open/ananke-core/ananke_core/ proprietary/living-cipher/app/ 2>/dev/null | grep -v "# FORBIDDEN" | grep -v "test" | grep -v "^[[:space:]]*#"; then
    fail "ML training code detected"
    FORBIDDEN_FOUND=1
fi

# Check for engagement terms (exclude comments, False assignments, and tests)
if grep -rn -E "engagement|retention|arousal" proprietary/living-cipher/app/ 2>/dev/null | \
   grep -v "False" | grep -v "# " | grep -v "test" | grep -v "addiction_metrics" | grep -v "^[[:space:]]*#"; then
    fail "Engagement optimization detected"
    FORBIDDEN_FOUND=1
fi

# Check for realism terms in renderer (exclude FORBIDDEN lists, comments, and "No X" documentation)
if grep -rn -E "photoreal|skin|face|eyes" proprietary/living-cipher/app/encode.py proprietary/living-cipher/render_gpu/*.py 2>/dev/null | \
   grep -v "FORBIDDEN" | grep -v "forbidden" | grep -v "No " | grep -v "NO " | grep -v "\- No" | \
   grep -v "#" | grep -v "not "; then
    fail "Realism terms in renderer"
    FORBIDDEN_FOUND=1
fi

if [ $FORBIDDEN_FOUND -eq 0 ]; then
    pass "No forbidden concepts detected"
fi

# 4️⃣ Dependency Check
section "4️⃣ Dependency Check"

# Check for ML frameworks
if grep -E "torch|tensorflow|keras|sklearn" open/ananke-core/requirements.txt proprietary/living-cipher/requirements.txt 2>/dev/null; then
    fail "ML framework in dependencies"
else
    pass "No ML frameworks in dependencies"
fi

# Check for analytics SDKs
if grep -E "google-analytics|mixpanel|segment|amplitude" proprietary/living-cipher/requirements.txt 2>/dev/null; then
    fail "Analytics SDK in dependencies"
else
    pass "No analytics SDKs in dependencies"
fi

# 5️⃣ Core Tests
section "5️⃣ Core Unit Tests"

if [ -d "open/ananke-core/tests" ] && [ "$(ls -A open/ananke-core/tests/*.py 2>/dev/null)" ]; then
    cd open/ananke-core
    if python -m pytest tests/ -q --tb=short 2>/dev/null; then
        pass "ananke-core tests passed"
    else
        fail "ananke-core tests failed"
    fi
    cd ../..
else
    warn "ananke-core tests not found (skipping)"
fi

# 6️⃣ Living Cipher Tests
section "6️⃣ Living Cipher Tests"

if [ -d "proprietary/living-cipher/tests" ] && [ "$(ls -A proprietary/living-cipher/tests/*.py 2>/dev/null)" ]; then
    cd proprietary/living-cipher
    if python -m pytest tests/ -q --tb=short 2>/dev/null; then
        pass "Living Cipher tests passed"
    else
        fail "Living Cipher tests failed"
    fi
    cd ../..
else
    warn "Living Cipher tests not found (skipping)"
fi

# 7️⃣ File Structure Verification
section "7️⃣ File Structure Verification"

REQUIRED_FILES=(
    "open/ananke-core/ananke_core/core.py"
    "open/ananke-core/ananke_core/video.py"
    "open/ananke-core/LICENSE"
    "proprietary/living-cipher/app/guards.py"
    "proprietary/living-cipher/app/flags.py"
    "proprietary/living-cipher/LICENSE"
    "docs/ethics.md"
    "docs/threat-model.md"
    ".github/workflows/ethics.yml"
)

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        pass "$file exists"
    else
        fail "$file missing"
    fi
done

# 8️⃣ Configuration Validation
section "8️⃣ Configuration Validation"

# Check that addiction monitoring is OFF by default
if grep -q 'ADDICTION_MONITORING = os.environ.get("AM_ENABLED", "false")' proprietary/living-cipher/app/addiction_metrics.py; then
    pass "Addiction monitoring defaults to OFF"
else
    warn "Addiction monitoring default unclear"
fi

# 9️⃣ Documentation Completeness
section "9️⃣ Documentation Completeness"

REQUIRED_DOCS=(
    "docs/architecture.md"
    "docs/ethics.md"
    "docs/threat-model.md"
    "docs/invariant-matrix.md"
    "docs/api-surface.md"
    "docs/clinical-mode.md"
    "docs/addiction-monitoring.md"
)

for doc in "${REQUIRED_DOCS[@]}"; do
    if [ -f "$doc" ]; then
        pass "$doc exists"
    else
        fail "$doc missing"
    fi
done

# 🔟 Final Verdict
section "🔟 Verification Summary"

echo ""
if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}✓ ALL CHECKS PASSED${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "System is verified and ready for:"
    echo "  • Production deployment"
    echo "  • Regulator engagement"
    echo "  • Public audit"
    echo "  • Scaling"
    echo ""
    echo "Ethics Anchor: $ETHICS_ANCHOR"
    echo ""
    exit 0
else
    echo -e "${RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${RED}✗ $FAILED CHECK(S) FAILED${NC}"
    echo -e "${RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "System NOT ready for production."
    echo "Review failures above and fix before deployment."
    echo ""
    exit 1
fi
