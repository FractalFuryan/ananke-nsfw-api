#!/bin/bash
# Clean commit plan for v1.0.0 release
# Execute this script to create atomic, audit-friendly commits

set -e

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📦 Ananke v1.0.0 Release Commit Plan"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check for uncommitted changes
if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "⚠️  Warning: You have uncommitted changes."
    echo "   Review with: git status"
    echo ""
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 1
    fi
fi

echo "Creating atomic commits for audit trail..."
echo ""

# Commit 1: Documentation updates
echo "📝 Commit 1/5: Core documentation (changelog, release notes, status)"
git add CHANGELOG.md RELEASE.md docs/STATUS.md
git commit -m "docs: add v1.0 changelog, release notes, system status

- Add CHANGELOG.md with complete v1.0.0 feature list
- Add RELEASE.md with installation and verification guide
- Add docs/STATUS.md with current system state
- Document all 7 hard invariants and verification status
- Include commit hash and timestamp references"

echo "✓ Committed"
echo ""

# Commit 2: README verification status
echo "📝 Commit 2/5: README verification status"
git add README.md
git commit -m "docs: update README with verification status

- Add verification status section after ethics checkpoint
- Include test pass rate (19/19)
- Add quick command reference
- Link to VERIFICATION.md, RELEASE.md, CHANGELOG.md
- Emphasize audit-ready state"

echo "✓ Committed"
echo ""

# Commit 3: Contributing guidelines
echo "📝 Commit 3/5: Contributing guidelines with ethics rules"
git add CONTRIBUTING.md
git commit -m "docs: add contributing guidelines with ethics enforcement

- Define non-negotiable ethics invariant
- List forbidden concepts (learning, personalization, engagement, realism)
- Document CI requirements and verification process
- Add development setup and PR workflow
- Clarify accepted vs rejected contribution types"

echo "✓ Committed"
echo ""

# Commit 4: Verification infrastructure
echo "📝 Commit 4/5: Phase 4 verification infrastructure"
git add verify.sh status.sh VERIFICATION.md Makefile docs/ATTESTATION.md docs/ATTESTATION-*.md .github/workflows/ethics.yml
git commit -m "feat: phase 4 verification infrastructure and attestation

- Add verify.sh: 10-section comprehensive verification script
- Add status.sh: quick system status check
- Add VERIFICATION.md: complete verification guide
- Enhance Makefile with 10 automation targets
- Add attestation system (template + generated reports)
- Update CI workflow with enhanced ethics checks
- All 19 tests passing (5 core + 14 cipher)"

echo "✓ Committed"
echo ""

# Commit 5: Test suite and verification fixes
echo "📝 Commit 5/5: Test suite and remaining updates"
git add open/ananke-core/tests/ proprietary/living-cipher/tests/ open/ananke-core/requirements.txt proprietary/living-cipher/requirements.txt
if git diff --staged --quiet; then
    echo "⚠️  No test changes to commit (already committed or no changes)"
else
    git commit -m "test: add comprehensive test suite for all layers

- Add ananke-core tests: determinism, video, invariants (5 tests)
- Add living-cipher tests: guards, modes, addiction metrics (14 tests)
- Update requirements.txt with pytest dependency
- 100% test pass rate achieved"
    echo "✓ Committed"
fi
echo ""

# Check if there are any remaining changes
if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "⚠️  Remaining uncommitted changes detected"
    echo ""
    git status --short
    echo ""
    read -p "Commit all remaining changes? (y/N) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git add .
        git commit -m "chore: finalize v1.0.0 release preparation"
        echo "✓ Committed remaining changes"
    else
        echo "Skipped remaining changes"
    fi
    echo ""
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ All commits created successfully"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Show commit log
echo "📋 Recent commits:"
git log --oneline -5
echo ""

# Tagging prompt
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🏷️  Release Tagging"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "To tag this release (recommended for trust):"
echo ""
echo "  git tag -a v1.0.0 -m \"Ananke NSFW API v1.0 — ethics-locked production release\""
echo "  git push origin v1.0.0"
echo ""

read -p "Create and push tag now? (y/N) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    git tag -a v1.0.0 -m "Ananke NSFW API v1.0 — ethics-locked production release"
    echo "✓ Tag created"
    
    read -p "Push to remote? (y/N) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git push origin main
        git push origin v1.0.0
        echo "✓ Pushed to remote"
    else
        echo "Tag created locally. Push later with: git push origin v1.0.0"
    fi
else
    echo "Skipped tagging. Create later with commands above."
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉 Release preparation complete!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Next steps:"
echo "  • Review commits: git log -p"
echo "  • Run verification: ./verify.sh"
echo "  • Generate attestation: make attestation"
echo "  • Deploy: make prod"
echo ""
