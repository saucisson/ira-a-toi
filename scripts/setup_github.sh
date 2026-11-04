#!/bin/bash
# Setup GitHub repository for "Ira à toi" project
# This script creates the repository, labels, milestones, and issues

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
REPO_NAME="ira-a-toi"
REPO_DESCRIPTION="Le nécessaire pour le dépôt - Collection 'Le Cabinet Noir'"
REPO_VISIBILITY="private"  # Change to "public" if needed
ORG_NAME=""  # Leave empty for user repo, set to org name if needed

# Get current directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo -e "${RED}Error: GitHub CLI (gh) is not installed.${NC}"
    echo "Install it from: https://cli.github.com/"
    exit 1
fi

# Check if authenticated
echo -e "${BLUE}Checking GitHub authentication...${NC}"
if ! gh auth status &> /dev/null; then
    echo -e "${RED}Error: Not authenticated with GitHub.${NC}"
    echo "Run: gh auth login"
    exit 1
fi

echo -e "${GREEN}✓ Authenticated with GitHub${NC}"

# Function to check if repo exists
repo_exists() {
    if [ -n "$ORG_NAME" ]; then
        gh repo view "$ORG_NAME/$REPO_NAME" &> /dev/null
    else
        gh repo view "$REPO_NAME" &> /dev/null
    fi
    return $?
}

# Step 1: Create repository or use existing
if repo_exists; then
    echo -e "${YELLOW}Repository '$REPO_NAME' already exists${NC}"
    if [ -n "$ORG_NAME" ]; then
        REPO_FULL_NAME="$ORG_NAME/$REPO_NAME"
    else
        REPO_FULL_NAME="$REPO_NAME"
    fi
else
    echo -e "${BLUE}Creating repository '$REPO_NAME'...${NC}"
    if [ -n "$ORG_NAME" ]; then
        gh repo create "$ORG_NAME/$REPO_NAME" --description "$REPO_DESCRIPTION" --visibility "$REPO_VISIBILITY" --push --source "." --confirm
    else
        gh repo create "$REPO_NAME" --description "$REPO_DESCRIPTION" --visibility "$REPO_VISIBILITY" --push --source "." --confirm
    fi
    REPO_FULL_NAME="$REPO_NAME"
    echo -e "${GREEN}✓ Repository created: $REPO_FULL_NAME${NC}"
fi

# Step 2: Push all branches and tags
cd "$PROJECT_DIR"
echo -e "${BLUE}Pushing all branches and tags to GitHub...${NC}"
git push --all origin
git push --tags origin
echo -e "${GREEN}✓ All branches and tags pushed${NC}"

# Step 3: Create labels
echo -e "${BLUE}Creating labels...${NC}"

# Priority labels
gh label create "priority: high" --color D73A4A --description "High priority - critical, blocks other work" --repo "$REPO_FULL_NAME"
gh label create "priority: medium" --color FBCA04 --description "Medium priority - important feature" --repo "$REPO_FULL_NAME"
gh label create "priority: low" --color 0E8A16 --description "Low priority - nice to have" --repo "$REPO_FULL_NAME"

# Category labels
gh label create "category: infrastructure" --color 6F42C1 --description "Infrastructure-related tasks (CI/CD, Docker, tooling)" --repo "$REPO_FULL_NAME"
gh label create "category: content" --color 1D76DB --description "Literary content tasks (works, fragments, enrichissements)" --repo "$REPO_FULL_NAME"
gh label create "category: frontend" --color 006B75 --description "Frontend development (React, TypeScript, UI)" --repo "$REPO_FULL_NAME"
gh label create "category: backend" --color 000000 --description "Backend development (Python, services, models)" --repo "$REPO_FULL_NAME"
gh label create "category: testing" --color E66600 --description "Testing-related tasks (unit tests, integration tests)" --repo "$REPO_FULL_NAME"
gh label create "category: documentation" --color 5319E7 --description "Documentation tasks (docs, ADRs, guides)" --repo "$REPO_FULL_NAME"
gh label create "category: validation" --color 11E109 --description "Validation tasks (contract validation, CI checks)" --repo "$REPO_FULL_NAME"
gh label create "category: design" --color FF77CC --description "Design tasks (interaction design, UX)" --repo "$REPO_FULL_NAME"
gh label create "category: research" --color 7C3AED --description "Research tasks (source finding, domain public verification)" --repo "$REPO_FULL_NAME"
gh label create "category: security" --color D93F0B --description "Security tasks (security audits, vulnerability fixes)" --repo "$REPO_FULL_NAME"
gh label create "category: agents" --color F98400 --description "Agent-related tasks (agent protocol, reviewer)" --repo "$REPO_FULL_NAME"
gh label create "category: maintenance" --color 576474 --description "Maintenance tasks (updates, backups, monitoring)" --repo "$REPO_FULL_NAME"
gh label create "category: ci" --color E66600 --description "Continuous Integration tasks" --repo "$REPO_FULL_NAME"

# Type labels
gh label create "type: feature" --color 1D76DB --description "New feature development" --repo "$REPO_FULL_NAME"
gh label create "type: bug" --color D73A4A --description "Bug fix" --repo "$REPO_FULL_NAME"
gh label create "type: chore" --color 576474 --description "Maintenance chore" --repo "$REPO_FULL_NAME"
gh label create "type: refactor" --color 6F42C1 --description "Code refactoring" --repo "$REPO_FULL_NAME"
gh label create "type: documentation" --color 5319E7 --description "Documentation work" --repo "$REPO_FULL_NAME"

# Work-specific labels
gh label create "work: le-horla" --color 1D76DB --description "Le Horla by Maupassant" --repo "$REPO_FULL_NAME"
gh label create "work: second-oeuvre" --color 0E8A16 --description "Second literary work" --repo "$REPO_FULL_NAME"
gh label create "work: third-oeuvre" --color 6F42C1 --description "Third literary work" --repo "$REPO_FULL_NAME"
gh label create "contract" --color E66600 --description "Contract schema work" --repo "$REPO_FULL_NAME"
gh label create "cadence" --color 6F42C1 --description "Cadence/pacing work" --repo "$REPO_FULL_NAME"
gh label create "ui" --color 006B75 --description "User interface work" --repo "$REPO_FULL_NAME"
gh label create "interactions" --color F98400 --description "Micro-interactions work" --repo "$REPO_FULL_NAME"
gh label create "assets" --color 11E109 --description "Assets (images, fonts, audio)" --repo "$REPO_FULL_NAME"

# Process labels
gh label create "needs-human" --color D73A4A --description "Requires human decision (per ADR-0011)" --repo "$REPO_FULL_NAME"
gh label create "blocked" --color D93F0B --description "Blocked by dependency" --repo "$REPO_FULL_NAME"
gh label create "escalation" --color E66600 --description "Escalated to human" --repo "$REPO_FULL_NAME"
gh label create "review" --color FBCA04 --description "Needs code/design review" --repo "$REPO_FULL_NAME"
gh label create "wip" --color 576474 --description "Work in progress" --repo "$REPO_FULL_NAME"
gh label create "ready" --color 0E8A16 --description "Ready for work" --repo "$REPO_FULL_NAME"
gh label create "duplicate" --color 576474 --description "Duplicate issue" --repo "$REPO_FULL_NAME"
gh label create "won't fix" --color 576474 --description "Will not be fixed" --repo "$REPO_FULL_NAME"
gh label create "good first issue" --color 0E8A16 --description "Beginner-friendly issue" --repo "$REPO_FULL_NAME"

# Agent-specific labels
gh label create "agent: developer" --color 1D76DB --description "Developer agent task" --repo "$REPO_FULL_NAME"
gh label create "agent: reviewer" --color 7C3AED --description "Reviewer agent task" --repo "$REPO_FULL_NAME"
gh label create "reviewer: blocking" --color D73A4A --description "BLOCKING finding" --repo "$REPO_FULL_NAME"
gh label create "reviewer: to-fix" --color FBCA04 --description "TO-FIX finding" --repo "$REPO_FULL_NAME"
gh label create "reviewer: suggestion" --color 0E8A16 --description "SUGGESTION finding" --repo "$REPO_FULL_NAME"
gh label create "attempt: 1" --color 576474 --description "First attempt" --repo "$REPO_FULL_NAME"
gh label create "attempt: 2" --color FBCA04 --description "Second attempt" --repo "$REPO_FULL_NAME"
gh label create "attempt: 3" --color D73A4A --description "Third and final attempt" --repo "$REPO_FULL_NAME"

echo -e "${GREEN}✓ All 47 labels created${NC}"

# Step 4: Create milestones
echo -e "${BLUE}Creating milestones...${NC}"

# M0: Project Infrastructure & Validation
gh api repos/$REPO_FULL_NAME/milestones \
  --method POST \
  --field title="M0: Project Infrastructure & Validation" \
  --field description="Ensure the template, CI/CD, and contract validation are fully operational." \
  --field due_on="$(date -d "+14 days" +%Y-%m-%dT00:00:00Z)" \
  --field state="open"

# M1: Complete Le Horla Pack
gh api repos/$REPO_FULL_NAME/milestones \
  --method POST \
  --field title="M1: Complete Le Horla Pack" \
  --field description="Finalize Maupassant's Le Horla pack with all 60+ entries." \
  --field due_on="$(date -d "+42 days" +%Y-%m-%dT00:00:00Z)" \
  --field state="closed"

# M2: First Additional Work
gh api repos/$REPO_FULL_NAME/milestones \
  --method POST \
  --field title="M2: First Additional Work" \
  --field description="Add a second literary work to the collection." \
  --field due_on="$(date -d "+63 days" +%Y-%m-%dT00:00:00Z)" \
  --field state="closed"

# M3: Frontend Integration
gh api repos/$REPO_FULL_NAME/milestones \
  --method POST \
  --field title="M3: Frontend Integration" \
  --field description="Connect the React/TypeScript frontend to the contract system." \
  --field due_on="$(date -d "+98 days" +%Y-%m-%dT00:00:00Z)" \
  --field state="closed"

# M4: Production Deployment
gh api repos/$REPO_FULL_NAME/milestones \
  --method POST \
  --field title="M4: Production Deployment" \
  --field description="Deploy to production CDN with all validated works." \
  --field due_on="$(date -d "+112 days" +%Y-%m-%dT00:00:00Z)" \
  --field state="closed"

# M5: Monitoring & Maintenance
gh api repos/$REPO_FULL_NAME/milestones \
  --method POST \
  --field title="M5: Monitoring & Maintenance" \
  --field description="Set up monitoring, analytics, and maintenance processes." \
  --field due_on="$(date -d "+126 days" +%Y-%m-%dT00:00:00Z)" \
  --field state="closed"

echo -e "${GREEN}✓ All 6 milestones created${NC}"

# Step 5: Create M0 issues
echo -e "${BLUE}Creating M0 issues...${NC}"

# Get milestone M0 ID
M0_ID=$(gh api repos/$REPO_FULL_NAME/milestones --jq '.[0].number')

# Function to create an issue
create_issue() {
    local title="$1"
    local body="$2"
    local labels="$3"
    
    gh issue create --repo "$REPO_FULL_NAME" \
        --title "$title" \
        --body "$body" \
        --label "$labels" \
        --milestone "M0: Project Infrastructure & Validation"
}

# M0-1: Setup GitHub Actions CI/CD workflows
create_issue "M0-1: Setup GitHub Actions CI/CD workflows" "## 📝 Description
Setup and verify all GitHub Actions workflows (ci.yml, mutation.yml, release.yml, review.yml).

## 🎯 Acceptance Criteria
- [ ] All workflows are configured in .github/workflows/
- [ ] ci.yml passes for all pushes to main and daily
- [ ] mutation.yml runs mutation testing
- [ ] release.yml handles version bumps and changelog
- [ ] review.yml launches reviewer agent

## 📌 Related
- **Milestone**: M0
- **Priority**: priority: high
- **Category**: category: infrastructure, category: ci-cd
- **Type**: type: chore

## ⚡ Estimated Effort
4 hours

## 📚 References
- .github/workflows/ directory
- docs/branching.md" "priority: high,category: infrastructure,category: ci-cd,type: chore"

# M0-2: Configure pre-commit hooks
create_issue "M0-2: Configure pre-commit hooks" "## 📝 Description
Configure pre-commit hooks for automatic code quality checks before commits.

## 🎯 Acceptance Criteria
- [ ] pre-commit installed and configured
- [ ] Hooks defined in .pre-commit-config.yaml
- [ ] pre-commit run --all-files passes on all files
- [ ] Hooks run automatically on git commit

## 📌 Related
- **Milestone**: M0
- **Priority**: priority: high
- **Category**: category: infrastructure, category: quality
- **Type**: type: chore

## ⚡ Estimated Effort
2 hours

## 📚 References
- .pre-commit-config.yaml
- pyproject.toml (dev dependencies)" "priority: high,category: infrastructure,category: quality,type: chore"

# M0-3: Verify make check on all environments
create_issue "M0-3: Verify make check on all environments" "## 📝 Description
Verify that make check passes locally and in CI for all supported environments.

## 🎯 Acceptance Criteria
- [ ] make lint passes (Ruff)
- [ ] make typecheck passes (mypy)
- [ ] make imports passes (import-linter)
- [ ] make test passes (pytest with 90%+ coverage)
- [ ] make web-check passes (if web dependencies installed)
- [ ] All checks pass in GitHub Actions CI

## 📌 Related
- **Milestone**: M0
- **Priority**: priority: high
- **Category**: category: infrastructure, category: testing
- **Type**: type: chore

## ⚡ Estimated Effort
4 hours

## 📚 References
- Makefile
- pyproject.toml (lint/type/config)" "priority: high,category: infrastructure,category: testing,type: chore"

# M0-4: Setup branch protection rules
create_issue "M0-4: Setup branch protection rules" "## 📝 Description
Configure branch protection for main and daily branches according to ADR-0010.

## 🎯 Acceptance Criteria
- [ ] main branch protected
- [ ] daily branch protected
- [ ] CI checks required for both branches
- [ ] No direct pushes to main or daily
- [ ] Auto-merge enabled for daily (if supported)

## 📌 Related
- **Milestone**: M0
- **Priority**: priority: high
- **Category**: category: infrastructure, git
- **Type**: type: chore

## ⚡ Estimated Effort
3 hours

## 📚 References
- docs/branching.md
- ADR-0010 (Branch model)" "priority: high,category: infrastructure,type: chore"

# M0-5: Validate release-please configuration
create_issue "M0-5: Validate release-please configuration" "## 📝 Description
Validate that release-please is properly configured for automated changelog generation.

## 🎯 Acceptance Criteria
- [ ] release-please-config.json is properly configured
- [ ] Conventional Commits format is enforced
- [ ] Version bump follows semantic versioning
- [ ] Changelog generation works automatically

## 📌 Related
- **Milestone**: M0
- **Priority**: priority: medium
- **Category**: category: infrastructure, category: release
- **Type**: type: chore

## ⚡ Estimated Effort
2 hours

## 📚 References
- release-please-config.json
- .github/workflows/release.yml" "priority: medium,category: infrastructure,category: release,type: chore"

# M0-6: Run CI validation on Le Horla pack
create_issue "M0-6: Run CI validation on Le Horla pack" "## 📝 Description
Run the CI validation script on the Le Horla pack to ensure it passes all checks.

## 🎯 Acceptance Criteria
- [ ] python ci/valider_pack.py oeuvres/le-horla-maupassant-1887 outputs PRÊT POUR PUBLICATION
- [ ] All 7 CI checks pass:
  - Anti-altération
  - Hash source
  - Fragments uniques
  - Cadences coverage
  - Références
  - Micro-interactions
  - Modèles Pydantic
- [ ] No errors or warnings

## 📌 Related
- **Milestone**: M0
- **Priority**: priority: high
- **Category**: category: validation, category: contract
- **Type**: type: chore

## ⚡ Estimated Effort
2 hours

## 📚 References
- ci/valider_pack.py
- contrat/pack.py
- oeuvres/le-horla-maupassant-1887/" "priority: high,category: validation,category: contract,type: chore"

# M0-7: Run full test suite
create_issue "M0-7: Run full test suite" "## 📝 Description
Run the complete test suite and ensure all tests pass.

## 🎯 Acceptance Criteria
- [ ] python -m unittest discover -s tests -v passes
- [ ] All 21 tests pass
- [ ] Coverage is 90% or higher
- [ ] No test failures or errors

## 📌 Related
- **Milestone**: M0
- **Priority**: priority: high
- **Category**: category: validation, category: testing
- **Type**: type: chore

## ⚡ Estimated Effort
2 hours

## 📚 References
- tests/test_contrat.py
- pyproject.toml (pytest config)" "priority: high,category: validation,category: testing,type: chore"

# M0-8: Verify mutation testing
create_issue "M0-8: Verify mutation testing" "## 📝 Description
Verify that mutation testing works and no critical mutants survive.

## 🎯 Acceptance Criteria
- [ ] make mutate runs without errors
- [ ] Mutation testing configured in pyproject.toml
- [ ] No surviving mutants in critical code paths
- [ ] Mutation score is acceptable

## 📌 Related
- **Milestone**: M0
- **Priority**: priority: medium
- **Category**: category: validation, category: testing
- **Type**: type: chore

## ⚡ Estimated Effort
4 hours

## 📚 References
- pyproject.toml (mutmut config)
- docs/decisions/adr-0013-anti-complacency-tests.md" "priority: medium,category: validation,category: testing,type: chore"

# M0-9: Create additional negative tests for contract
create_issue "M0-9: Create additional negative tests for contract" "## 📝 Description
Create negative tests to ensure all contract invariants properly reject invalid data.

## 🎯 Acceptance Criteria
- [ ] All invariants in contrat/pack.py have corresponding negative tests
- [ ] Tests cover:
  - Anti-altération (text modification)
  - Invalid IDs (non-slug)
  - Missing fragments
  - Invalid references
  - Missing conditions/effects
  - Invalid corruption targets
- [ ] Test coverage for contract validation is 100%

## 📌 Related
- **Milestone**: M0
- **Priority**: priority: medium
- **Category**: category: validation, category: testing, category: contract
- **Type**: type: chore

## ⚡ Estimated Effort
8 hours

## 📚 References
- contrat/pack.py
- tests/test_contrat.py" "priority: medium,category: validation,category: testing,category: contract,type: chore"

# M0-10: Document contract schema v1.1
create_issue "M0-10: Document contract schema v1.1" "## 📝 Description
Create comprehensive documentation for the contract schema v1.1.

## 🎯 Acceptance Criteria
- [ ] All fields in Pack, Manifeste, Fragment, etc. are documented
- [ ] Examples provided for each field
- [ ] Invariant rules clearly explained
- [ ] Domain public requirements documented
- [ ] Documentation linked from README.md

## 📌 Related
- **Milestone**: M0
- **Priority**: priority: medium
- **Category**: category: documentation, category: contract
- **Type**: type: documentation

## ⚡ Estimated Effort
4 hours

## 📚 References
- contrat/pack.py
- ASSISTANCE_IA.md §2-5" "priority: medium,category: documentation,category: contract,type: documentation"

# M0-11: Setup reviewer agent workflow
create_issue "M0-11: Setup reviewer agent workflow" "## 📝 Description
Setup the reviewer agent workflow to automatically review pull requests.

## 🎯 Acceptance Criteria
- [ ] review.yml workflow is properly configured
- [ ] Reviewer agent runs on all PRs to daily branch
- [ ] Reviewer exit code determines merge status
- [ ] Review reports contain BLOCKING/TO-FIX/SUGGESTION findings
- [ ] 0 BLOCKING findings required for merge

## 📌 Related
- **Milestone**: M0
- **Priority**: priority: high
- **Category**: category: agents, category: infrastructure
- **Type**: type: chore

## ⚡ Estimated Effort
4 hours

## 📚 References
- .github/workflows/review.yml
- docs/agents/reviewer.md
- docs/decisions/adr-0016-reviewer-launch-mechanics.md" "priority: high,category: agents,category: infrastructure,type: chore"

# M0-12: Test day cycle automation
create_issue "M0-12: Test day cycle automation" "## 📝 Description
Test the day cycle automation commands (day-start, day-report, smoke-test).

## 🎯 Acceptance Criteria
- [ ] make day-start creates daily-YYYY-MM-DD tag
- [ ] make day-report shows activity since morning tag
- [ ] make smoke-test verifies notification pipeline
- [ ] All commands work in CI environment
- [ ] Commands are documented in NEXT_STEPS.md

## 📌 Related
- **Milestone**: M0
- **Priority**: priority: high
- **Category**: category: agents, category: process
- **Type**: type: chore

## ⚡ Estimated Effort
4 hours

## 📚 References
- Makefile (day-start, day-report, smoke-test)
- scripts/day_report.py
- scripts/build_review_bundle.py
- tools/notify/" "priority: high,category: agents,category: process,type: chore"

echo -e "${GREEN}✓ All 12 M0 issues created${NC}"

# Step 6: Setup branch protection
echo -e "${BLUE}Setting up branch protection...${NC}"

# Protect main branch
gh api repos/$REPO_FULL_NAME/branches/main/protection \
  --method PUT \
  --field "{\"required_status_checks\": {\"strict\": true, \"contexts\": [\"check\", \"web\"]}, \"enforce_admins\": true, \"required_pull_request_reviews\": {\"dismiss_stale_reviews\": true, \"require_code_owner_reviews\": false}, \"restrictions\": null}"

# Protect daily branch
gh api repos/$REPO_FULL_NAME/branches/daily/protection \
  --method PUT \
  --field "{\"required_status_checks\": {\"strict\": true, \"contexts\": [\"check\", \"web\"]}, \"enforce_admins\": true, \"required_pull_request_reviews\": {\"dismiss_stale_reviews\": true, \"require_code_owner_reviews\": false}, \"restrictions\": null}"

echo -e "${GREEN}✓ Branch protection configured for main and daily${NC}"

# Step 7: Create daily branch
echo -e "${BLUE}Creating daily branch...${NC}"
cd "$PROJECT_DIR"
git checkout -b daily
git push origin daily
echo -e "${GREEN}✓ Daily branch created and pushed${NC}"

# Return to main
git checkout main

echo ""
echo -e "${GREEN}==========================================${NC}"
echo -e "${GREEN}✅ GitHub setup completed successfully!${NC}"
echo -e "${GREEN}==========================================${NC}"
echo ""
echo -e "Repository: $REPO_FULL_NAME"
echo -e "Labels: 47 created"
echo -e "Milestones: 6 created (M0-M5)"
echo -e "Issues: 12 M0 issues created"
echo -e "Branches: main (protected), daily (protected)"
echo ""
echo -e "Next steps:"
echo "1. Open $REPO_FULL_NAME in your browser"
echo "2. Verify all labels, milestones, and issues exist"
echo "3. Assign issues to team members"
echo "4. Start working on M0-1: Setup GitHub Actions CI/CD workflows"
echo ""
echo -e "Run 'gh repo view --web' to open the repository in your browser."
