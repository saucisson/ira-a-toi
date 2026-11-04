# Next Steps for "Ira à toi" Project

> **Status**: ✅ Initial commit created | 📋 Project plan documented | ⏭️ Ready for GitLab setup

---

## ✅ Completed

### 1. Git Repository Initialized
- **Commit 1**: `541b3e6` - Initial project setup
  - All template files committed
  - Contract schema v1.1 included
  - Example pack (Le Horla) included
  - Complete documentation added
  - CI/CD configuration in place

- **Commit 2**: `a8d3f65` - Project plan documented
  - `.gitlab/PROJECT_PLAN.md` - 6 milestones with detailed issues
  - `.gitlab/ISSUE_TEMPLATES.md` - Ready-to-use issue templates
  - `.gitlab/LABELS.md` - Complete label configuration guide

---

## 🎯 Immediate Next Steps (Priority Order)

### 1️⃣ **Setup GitLab Project** (Critical - Blocking)
**Estimated Time**: 15-30 minutes

#### Actions:
1. **Create GitLab project** (if not already created):
   - Go to GitLab → New Project
   - Name: `ira-a-toi`
   - Visibility: Private (or Internal)
   - Initialize with README: ❌ (we have our own)
   - Import existing repository: ✅ (use local path)

2. **Push local repository to GitLab**:
   ```bash
   cd /home/alban/ira-a-toi
   git remote add origin git@gitlab.com:<username>/ira-a-toi.git
   git push -u origin main
   ```

3. **Verify remote**:
   ```bash
   git remote -v
   git fetch origin
   ```

---

### 2️⃣ **Setup GitLab Configuration** (Critical - Blocking)
**Estimated Time**: 30-60 minutes

#### Actions:
1. **Create Labels**:
   - Use `.gitlab/LABELS.md` as reference
   - Create all labels via GitLab UI (Settings → General → Labels)
   - **Priority**: Start with Priority labels (`priority:high`, `priority:medium`, `priority:low`)

2. **Create Milestones**:
   - Use `.gitlab/PROJECT_PLAN.md` → Milestones section
   - Create all 6 milestones (M0-M5) with descriptions and due dates
   - **Priority**: Start with M0 (Infrastructure & Validation)

3. **Create Issues**:
   - Start with **M0 issues** (infrastructure and validation)
   - Use templates from `.gitlab/ISSUE_TEMPLATES.md`
   - **Recommended first batch**:
     - M0-1: Setup GitLab CI/CD pipeline
     - M0-2: Configure pre-commit hooks
     - M0-3: Verify `make check` on all environments
     - M0-6: Run CI validation on Le Horla pack
     - M0-7: Run full test suite
     - M0-11: Setup reviewer agent workflow

4. **Configure CI/CD Variables**:
   - Go to Settings → CI/CD → Variables
   - Add any required secrets (Discord webhook, etc.)

---

### 3️⃣ **Verify Local Environment** (High Priority)
**Estimated Time**: 1-2 hours

#### Actions:
1. **Install dependencies**:
   ```bash
   make install
   ```
   - This runs `uv sync --locked` and sets up pre-commit hooks

2. **Run quality gates locally**:
   ```bash
   make check
   ```
   - This runs: lint + typecheck + imports + test + web-check
   - **Expected**: All checks should pass

3. **Test the contract validation**:
   ```bash
   python ci/valider_pack.py oeuvres/le-horla-maupassant-1887
   ```
   - **Expected output**: "PRÊT POUR PUBLICATION"

4. **Run tests**:
   ```bash
   python -m unittest discover -s tests -v
   ```
   - **Expected**: All 21 tests pass

5. **Test web frontend** (if Node.js available):
   ```bash
   cd apps/web
   npm install
   npm run dev
   ```
   - Open `http://localhost:5173` to verify

---

### 4️⃣ **Setup Branch Protection** (High Priority)
**Estimated Time**: 10 minutes

#### Actions (in GitLab):
1. **Protect `main` branch**:
   - Settings → Repository → Protected Branches
   - Branch: `main`
   - Allowed to merge: Maintainers/Owners only
   - Allowed to push: No one
   - Require CI to pass: ✅
   - Require approvals: ❌ (handled by reviewer agent)

2. **Create `daily` branch**:
   ```bash
   git checkout -b daily
   git push origin daily
   ```

3. **Protect `daily` branch**:
   - Settings → Repository → Protected Branches
   - Branch: `daily`
   - Allowed to merge: Maintainers/Owners only
   - Allowed to push: No one
   - Require CI to pass: ✅

4. **Configure branch protections for workflows**:
   - Ensure `ci.yml`, `review.yml` workflows are required

---

### 5️⃣ **Setup Day Cycle Automation** (Medium Priority)
**Estimated Time**: 15 minutes

#### Actions:
1. **Test day cycle commands**:
   ```bash
   make day-start
   ```
   - Creates tag: `daily-YYYY-MM-DD`
   - Verify tag exists: `git tag -l`

2. **Test day report**:
   ```bash
   make day-report
   ```
   - Shows activity since the morning tag
   - **Note**: Will show "no commits" if run immediately after day-start

3. **Test smoke test**:
   ```bash
   make smoke-test
   ```
   - Verifies notification pipeline
   - **Expected**: Console output with success message

---

## 📋 M0: Infrastructure & Validation Checklist

Start with these issues from `.gitlab/PROJECT_PLAN.md`:

| Issue | Priority | Effort | Status | Notes |
|-------|----------|--------|--------|-------|
| M0-1 | High | 4h | ⬜ To Do | Setup GitLab CI/CD pipeline |
| M0-2 | High | 2h | ⬜ To Do | Configure pre-commit hooks |
| M0-3 | High | 4h | ⬜ To Do | Verify `make check` on all environments |
| M0-4 | Medium | 3h | ⬜ To Do | Setup Docker Compose for local development |
| M0-5 | Medium | 2h | ⬜ To Do | Validate release-please configuration |
| M0-6 | High | 2h | ⬜ To Do | Run CI validation on Le Horla pack |
| M0-7 | High | 2h | ⬜ To Do | Run full test suite |
| M0-8 | Medium | 4h | ⬜ To Do | Verify mutation testing |
| M0-9 | Medium | 8h | ⬜ To Do | Create additional negative tests |
| M0-10 | Medium | 4h | ⬜ To Do | Document contract schema |
| M0-11 | High | 4h | ⬜ To Do | Setup reviewer agent workflow |
| M0-12 | High | 4h | ⬜ To Do | Test day cycle automation |

**Total M0 Effort**: ~45 hours

---

## 🚀 Quick Start Guide

### For Immediate Local Testing:

1. **Verify Python version** (≥ 3.15):
   ```bash
   python --version
   ```

2. **Install uv** (if not installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Install project dependencies**:
   ```bash
   make install
   ```

4. **Run quality checks**:
   ```bash
   make check
   ```

5. **Validate the example pack**:
   ```bash
   python ci/valider_pack.py oeuvres/le-horla-maupassant-1887
   ```

---

## 📅 Suggested Week 1 Plan

### Day 1: Project Setup
- [ ] Push repository to GitLab
- [ ] Create labels in GitLab
- [ ] Create M0 milestone
- [ ] Create M0 issues (M0-1 to M0-5)
- [ ] Verify local environment (`make install`, `make check`)

### Day 2: CI/CD Setup
- [ ] Fix any issues from `make check`
- [ ] Setup GitLab CI/CD variables
- [ ] Verify GitLab CI pipeline passes
- [ ] Create M0 issues (M0-6 to M0-12)

### Day 3: Validation
- [ ] Run all tests locally
- [ ] Run CI validation on Le Horla pack
- [ ] Setup pre-commit hooks
- [ ] Test day cycle commands

### Day 4-5: Documentation & Cleanup
- [ ] Complete M0 documentation
- [ ] Create README for src/ directory
- [ ] Review and refine project plan
- [ ] Begin M1 planning

---

## 🎯 Success Criteria for Week 1

- ✅ Repository pushed to GitLab with all history
- ✅ All labels created in GitLab
- ✅ M0 milestone created with all issues
- ✅ Local environment fully functional (`make check` passes)
- ✅ GitLab CI pipeline green
- ✅ Le Horla pack validates successfully
- ✅ Day cycle automation tested

---

## 📊 Current Project State

### Git Status
```
Commit History:
  a8d3f65 docs: add project plan with milestones, issues, and labels
  541b3e6 feat: initial project setup with template, contract, and example pack

Branch: main
Status: Clean (nothing to commit)
```

### Files Created
- **108 files** in initial commit
- **3 files** in project plan commit
- **Total: 111 files**

### Key Directories
- `contrat/` - Work contract schema (pack.py)
- `ci/` - CI validation scripts
- `oeuvres/` - Literary works (Le Horla example)
- `tools/notify/` - Agent notification system
- `apps/web/` - React/TypeScript frontend
- `docs/` - Architecture, ADRs, review checklist
- `scripts/` - Day cycle and review orchestration
- `.gitlab/` - GitLab-specific configurations and plans

---

## 🔗 Important Links & References

### Project Documentation
- `AGENTS.md` - Agent constitution and protocol
- `ASSISTANCE_IA.md` - AI assistance rules for this project
- `docs/architecture.md` - Architecture and style rules
- `docs/branching.md` - Branch model and day cycle
- `docs/review-checklist.md` - Review checklist for agents
- `docs/decisions/` - Architecture Decision Records (ADRs)

### Quick Commands
| Command | Description |
|---------|-------------|
| `make help` | List all available make targets |
| `make install` | Install dependencies and pre-commit hooks |
| `make check` | Run all quality gates (lint, typecheck, imports, tests) |
| `make lint` | Run Ruff linter |
| `make typecheck` | Run mypy type checker |
| `make imports` | Verify onion layer contract |
| `make test` | Run all tests with coverage |
| `make web-check` | Web frontend quality gate |
| `make day-start` | Start the day (create restore point tag) |
| `make day-report` | Generate end-of-day report |
| `make smoke-test` | Verify notification pipeline |

---

## 💡 Tips & Best Practices

1. **Follow Conventional Commits**: All commit messages must follow the format `type(scope): message`

2. **Respect the Onion Architecture**: Dependencies must point inward only (models → services → infrastructure → main)

3. **Never Modify Source Text**: The CI will catch any alteration of the original text

4. **Always Validate Packs**: Run `ci/valider_pack.py` after any change to a work

5. **Use the Templates**: The issue templates and labels are designed to work with the agent protocol

6. **Document Domain Public Proof**: Every asset must include proof of domain public status

7. **Test Negative Cases**: Every new invariant should have a corresponding negative test

---

## 🎯 What's Blocking Progress?

| Item | Status | Blocked By | Next Action |
|------|--------|------------|-------------|
| GitLab project | ❌ Not created | User action | Create project and push |
| Labels | ❌ Not created | GitLab project | Create in GitLab UI |
| Milestones | ❌ Not created | GitLab project | Create in GitLab UI |
| Issues | ❌ Not created | Labels/Milestones | Create using templates |
| Branch protection | ❌ Not configured | GitLab project | Configure in Settings |

**⚠️ All other work is blocked until the GitLab project is set up and the repository is pushed.**

---

## 🏁 Ready to Start?

Once the GitLab project is set up and the repository is pushed:

1. **Create labels** (from `.gitlab/LABELS.md`)
2. **Create milestones** (from `.gitlab/PROJECT_PLAN.md`)
3. **Create M0 issues** (from `.gitlab/PROJECT_PLAN.md`)
4. **Assign issues** to yourself or team members
5. **Start with M0-1**: Setup GitLab CI/CD pipeline

---

## 📞 Need Help?

If you encounter any issues:

1. **Check the documentation**: All project rules are in `AGENTS.md`, `ASSISTANCE_IA.md`, and `docs/`

2. **Review the ADRs**: Architecture decisions are documented in `docs/decisions/`

3. **Check the contract**: The work contract is in `contrat/pack.py`

4. **Run the validation**: `python ci/valider_pack.py oeuvres/le-horla-maupassant-1887`

5. **Ask for clarification**: Use the issue templates to create a `needs-human` issue if something is unclear

---

*This document is a living guide. Update it as the project progresses.*
