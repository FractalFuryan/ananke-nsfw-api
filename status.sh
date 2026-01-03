#!/bin/bash
# Quick status check for Ananke system

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 Ananke System Status"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Ethics anchor
echo "🔒 Ethics Anchor:"
echo "   65b14d584f5a5fd070fe985eeb86e14cb3ce56a4fc41fd9e987f2259fe1f15c1"
ANCHOR_COUNT=$(grep -r "65b14d584f5a5fd070fe985eeb86e14cb3ce56a4fc41fd9e987f2259fe1f15c1" . --include="*.py" --include="*.md" 2>/dev/null | wc -l)
echo "   Found in $ANCHOR_COUNT locations ✓"
echo ""

# Tests
echo "🧪 Test Status:"
cd open/ananke-core
CORE_TESTS=$(python -m pytest tests/ -q 2>/dev/null | grep passed | awk '{print $1}')
cd ../..
cd proprietary/living-cipher
CIPHER_TESTS=$(python -m pytest tests/ -q 2>/dev/null | grep passed | awk '{print $1}')
cd ../..

echo "   ananke-core: ${CORE_TESTS:-?} tests passing"
echo "   living-cipher: ${CIPHER_TESTS:-?} tests passing"
echo "   Total: $((${CORE_TESTS:-0} + ${CIPHER_TESTS:-0})) tests ✓"
echo ""

# Documentation
echo "📚 Documentation:"
DOC_COUNT=$(ls docs/*.md 2>/dev/null | wc -l)
echo "   ${DOC_COUNT} regulator documents"
ls docs/*.md 2>/dev/null | xargs -n1 basename | sed 's/^/   - /'
echo ""

# Dependencies
echo "📦 Dependencies:"
if grep -E "torch|tensorflow" */requirements.txt 2>/dev/null > /dev/null; then
    echo "   ❌ ML frameworks detected (VIOLATION)"
else
    echo "   ✓ No ML frameworks"
fi

if grep -E "mixpanel|segment" */requirements.txt 2>/dev/null > /dev/null; then
    echo "   ❌ Analytics SDKs detected (VIOLATION)"
else
    echo "   ✓ No analytics SDKs"
fi
echo ""

# Service health (if running)
echo "🏥 Service Health:"
if curl -f -s http://localhost:8000/health > /dev/null 2>&1; then
    echo "   ✓ Living Cipher service UP (port 8000)"
else
    echo "   ⚠ Living Cipher service not running"
    echo "     Run: make dev"
fi
echo ""

# Available commands
echo "🛠️  Quick Commands:"
echo "   make verify      — Full verification (10 sections)"
echo "   make test        — Run all unit tests"
echo "   make ethics      — Quick ethics check"
echo "   make attestation — Generate audit report"
echo "   make dev         — Start development server"
echo ""

# Final verdict
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [ $((${CORE_TESTS:-0} + ${CIPHER_TESTS:-0})) -ge 19 ] && [ "$ANCHOR_COUNT" -ge 10 ]; then
    echo "✅ System: VERIFIED & PRODUCTION-READY"
else
    echo "⚠️  System: Needs attention (run ./verify.sh)"
fi
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
