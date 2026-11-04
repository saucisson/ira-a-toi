# Next Steps for "Ira à toi" Project (GitHub)

> **Status**: ✅ Initial commit created | 📋 Project plan documented | ⏭️ Ready for GitHub setup
> **Platform**: **GitHub** (not GitLab)

---

## ✅ Completed

### 1. Git Repository Initialized
- **Commit 1**: `541b3e6` - Initial project setup
  - All template files committed
  - Contract schema v1.1 included
  - Example pack (Le Horla) included
  - Complete documentation added
  - CI/CD configuration in place

- **Commit 2**: `a8d3f65` - Project plan documented (GitLab version - deprecated)
  - *Note: Replaced by GitHub-specific files*

- **Commit 3**: `9480191` - Next steps guide (GitLab version - deprecated)
  - *Note: Being replaced by this GitHub-specific version*

- **New Files**: GitHub-specific documentation in `.github/`
  - `.github/PROJECT_PLAN.md` - Milestones and issues for GitHub
  - `.github/ISSUE_TEMPLATES.md` - GitHub issue templates
  - `.github/LABELS.md` - GitHub label configuration

---

## 🎯 Immediate Next Steps (Priority Order)

### 1️⃣ **Setup GitHub Repository** (Critical - Blocking)
**Estimated Time**: 15-30 minutes

#### Actions:
1. **Create GitHub repository** (if not already created):
   - Go to [GitHub](https://github.com) → New Repository
   - Name: `ira-a-toi`
   - Description: `Le nécessaire pour le dépôt - Collection "Le Cabinet Noir"`
   - Public/Private: **Private** (recommended for development)
   - Initialize with README: ❌ (we have our own)
   - Add .gitignore: ❌ (we have our own)
   - License: ❌ (already included)

2. **Push local repository to GitHub**:
   ```bash
   cd /home/alban/ira-a-toi
   git remote add origin git@github.com:<votre-utilisateur>/ira-a-toi.git
   git push -u origin main
   ```

3. **Verify remote**:
   ```bash
   git remote -v
   git fetch origin
   ```

4. **Enable GitHub Actions**:
   - Go to **Settings → Actions → General**
   - Ensure "Actions permissions" is set to **Read and write permissions**
   - Enable workflows

---

### 2️⃣ **Setup GitHub Configuration** (Critical - Blocking)
**Estimated Time**: 30-60 minutes

#### Actions:
1. **Create Labels**:
   - Use `.github/LABELS.md` as reference
   - Go to **Settings → Issues → Labels → New label**
   - Create all labels with exact names and colors
   - **Priority**: Start with Priority labels, then Type, then Category

2. **Create Milestones**:
   - Use `.github/PROJECT_PLAN.md` → Milestones section
   - Go to **Issues → Milestones → New milestone**
   - Create all 6 milestones (M0-M5) with descriptions
   - **Priority**: Start with M0 (Infrastructure & Validation)
   - Set due dates based on your timeline

3. **Create Issues**:
   - Start with **M0 issues** (infrastructure and validation)
   - Go to **Issues → New issue**
   - Use templates from `.github/ISSUE_TEMPLATES.md`
   - **Recommended first batch**:
     - M0-1: Setup GitHub Actions CI/CD workflows
     - M0-2: Configure pre-commit hooks
     - M0-3: Verify `make check` on all environments
     - M0-4: Setup branch protection rules
     - M0-6: Run CI validation on Le Horla pack
     - M0-7: Run full test suite
     - M0-11: Setup reviewer agent workflow
   - Assign each issue to:
     - **Milestone**: M0
     - **Labels**: From LABELS.md (e.g., `priority: high`, `category: infrastructure`, `type: chore`)
     - **Assignees**: Yourself or team members

4. **Configure Branch Protection**:
   - Go to **Settings → Branches → Branch protection rules → Add rule**
   - **For `main` branch**:
     - Branch name pattern: `main`
     - Require a pull request before merging: ✅
     - Require approvals: ❌ (handled by reviewer agent)
     - Dismiss stale pull request approvals when new commits are pushed: ✅
     - Require status checks to pass before merging: ✅
       - Select: `check` job, `web` job
     - Include administrators: ✅
     - Restrict who can push to matching branches: ✅
       - Select: Only you (or specific users)
   - **For `daily` branch**:
     - Branch name pattern: `daily`
     - Same settings as `main`
     - Additionally: Allow auto-merge: ✅

5. **Configure GitHub Actions Secrets** (if needed):
   - Go to **Settings → Secrets and variables → Actions → New repository secret**
   - Add any required secrets (e.g., `DISCORD_WEBHOOK_URL` for notifications)

---

### 3️⃣ **Create the `daily` Branch** (High Priority)
**Estimated Time**: 5 minutes

#### Actions:
1. **Create and push `daily` branch**:
   ```bash
   git checkout -b daily
   git push origin daily
   ```

2. **Verify branch protection**:
   - Go to **Settings → Branches**
   - Verify both `main` and `daily` have protection rules

---

### 4️⃣ **Verify Local Environment** (High Priority)
**Estimated Time**: 1-2 hours

#### Actions:
1. **Install dependencies**:
   ```bash
   make install
   ```
   - This runs `uv sync --locked` and sets up pre-commit hooks
   - **Note**: Requires Python 3.15+ and uv

2. **Install uv** (if not installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Run quality gates locally**:
   ```bash
   make check
   ```
   - This runs: lint + typecheck + imports + test + web-check
   - **Expected**: All checks should pass
   - If any fail, fix the issues before proceeding

4. **Test the contract validation**:
   ```bash
   python ci/valider_pack.py oeuvres/le-horla-maupassant-1887
   ```
   - **Expected output**: "PRÊT POUR PUBLICATION"

5. **Run tests**:
   ```bash
   python -m unittest discover -s tests -v
   ```
   - **Expected**: All 21 tests pass

6. **Test web frontend** (if Node.js available):
   ```bash
   cd apps/web
   npm install
   npm run dev
   ```
   - Open `http://localhost:5173` to verify
   - **Note**: Frontend is optional for M0

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
   - **Note**: Requires notify tool to be installed (`make install`)

---

## 📋 M0: Infrastructure & Validation Checklist

Start with these issues from `.github/PROJECT_PLAN.md`:

| Issue | Priority | Labels | Effort | Status | Notes |
|-------|----------|--------|--------|--------|-------|
| M0-1 | High | `priority: high`, `category: infrastructure`, `category: ci-cd`, `type: chore` | 4h | ⬜ To Do | Setup GitHub Actions CI/CD workflows |
| M0-2 | High | `priority: high`, `category: infrastructure`, `category: quality`, `type: chore` | 2h | ⬜ To Do | Configure pre-commit hooks |
| M0-3 | High | `priority: high`, `category: infrastructure`, `category: testing`, `type: chore` | 4h | ⬜ To Do | Verify `make check` on all environments |
| M0-4 | High | `priority: high`, `category: infrastructure`, `type: chore` | 3h | ⬜ To Do | Setup branch protection rules |
| M0-5 | Medium | `priority: medium`, `category: infrastructure`, `category: release`, `type: chore` | 2h | ⬜ To Do | Validate release-please configuration |
| M0-6 | High | `priority: high`, `category: validation`, `category: contract`, `type: chore` | 2h | ⬜ To Do | Run CI validation on Le Horla pack |
| M0-7 | High | `priority: high`, `category: validation`, `category: testing`, `type: chore` | 2h | ⬜ To Do | Run full test suite |
| M0-8 | Medium | `priority: medium`, `category: validation`, `category: testing`, `type: chore` | 4h | ⬜ To Do | Verify mutation testing |
| M0-9 | Medium | `priority: medium`, `category: validation`, `category: testing`, `type: chore` | 8h | ⬜ To Do | Create additional negative tests |
| M0-10 | Medium | `priority: medium`, `category: documentation`, `category: contract`, `type: documentation` | 4h | ⬜ To Do | Document contract schema |
| M0-11 | High | `priority: high`, `category: agents`, `category: infrastructure`, `type: chore` | 4h | ⬜ To Do | Setup reviewer agent workflow |
| M0-12 | High | `priority: high`, `category: agents`, `category: process`, `type: chore` | 4h | ⬜ To Do | Test day cycle automation |

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

### Day 1: GitHub Setup
- [ ] Push repository to GitHub
- [ ] Enable GitHub Actions
- [ ] Create labels in GitHub (all 47 labels from LABELS.md)
- [ ] Create M0 milestone
- [ ] Create M0 issues (M0-1 to M0-5)
- [ ] Verify local environment (`make install`)

### Day 2: CI/CD Setup
- [ ] Fix any issues from `make check`
- [ ] Verify GitHub Actions workflows pass
- [ ] Create M0 issues (M0-6 to M0-12)
- [ ] Setup branch protection for `main` and `daily`
- [ ] Create `daily` branch

### Day 3: Validation
- [ ] Run all tests locally
- [ ] Run CI validation on Le Horla pack
- [ ] Setup pre-commit hooks
- [ ] Test day cycle commands
- [ ] Verify GitHub Actions CI passes

### Day 4-5: Documentation & Cleanup
- [ ] Complete M0 documentation
- [ ] Create README for src/ directory
- [ ] Review and refine project plan
- [ ] Begin M1 planning (Le Horla completion)

---

## 🎯 Success Criteria for Week 1

- ✅ Repository pushed to GitHub with all history
- ✅ All 47 labels created in GitHub
- ✅ M0 milestone created with all 12 issues
- ✅ Local environment fully functional (`make check` passes)
- ✅ GitHub Actions CI pipeline green
- ✅ Le Horla pack validates successfully
- ✅ Branch protection configured for `main` and `daily`
- ✅ Day cycle automation tested

---

## 📊 Current Project State

### Git Status
```
Commit History:
  9480191 docs: add next steps guide for project initialization
  a8d3f65 docs: add project plan with milestones, issues, and labels
  541b3e6 feat: initial project setup with template, contract, and example pack

Branch: main
Status: Clean (nothing to commit)

New Files (GitHub-specific):
  .github/PROJECT_PLAN.md
  .github/ISSUE_TEMPLATES.md
  .github/LABELS.md
```

### Files Created
- **108 files** in initial commit
- **3 files** in project plan commit (GitLab - to be removed)
- **1 file** in next steps commit (GitLab - to be replaced)
- **3 files** in GitHub-specific commit
- **Total: 115 files**

### Key Directories
- `contrat/` - Work contract schema (pack.py)
- `ci/` - CI validation scripts
- `oeuvres/` - Literary works (Le Horla example)
- `tools/notify/` - Agent notification system
- `apps/web/` - React/TypeScript frontend
- `docs/` - Architecture, ADRs, review checklist
- `scripts/` - Day cycle and review orchestration
- `.github/` - **GitHub-specific configurations and plans**

---

## 🔗 Important Links & References

### GitHub Setup
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Labels Documentation](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels)
- [GitHub Milestones Documentation](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-milestones)
- [Branch Protection Documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)

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
| `make check` | **Run all quality gates** (lint, typecheck, imports, tests) |
| `make lint` | Run Ruff linter |
| `make typecheck` | Run mypy type checker |
| `make imports` | Verify onion layer contract |
| `make test` | Run all tests with coverage |
| `make web-check` | Web frontend quality gate |
| `python ci/valider_pack.py oeuvres/le-horla-maupassant-1887` | **Validate the Le Horla pack** |
| `git push origin main` | Push to GitHub main branch |
| `git push origin daily` | Push to GitHub daily branch |

---

## 💡 Tips & Best Practices

1. **Follow Conventional Commits**: All commit messages must follow the format `type(scope): message`

2. **Respect the Onion Architecture**: Dependencies must point inward only (models → services → infrastructure → main)

3. **Never Modify Source Text**: The CI will catch any alteration of the original text

4. **Always Validate Packs**: Run `ci/valider_pack.py` after any change to a work

5. **Use the Templates**: The issue templates and labels are designed to work with the agent protocol

6. **Document Domain Public Proof**: Every asset must include proof of domain public status

7. **Test Negative Cases**: Every new invariant should have a corresponding negative test

8. **GitHub-specific**: Use GitHub's features like milestones, projects, and issue tracking

---

## ⚠️ What's Blocking Progress?

**Aucun travail supplémentaire ne peut commencer tant que** :

| Item | Status | Blocked By | Next Action |
|------|--------|------------|-------------|
| GitHub repository | ❌ Not created | User action | Create repository and push |
| Labels | ❌ Not created | GitHub repository | Create in GitHub Settings |
| Milestones | ❌ Not created | GitHub repository | Create in GitHub Issues |
| Issues | ❌ Not created | Labels/Milestones | Create using templates |
| Branch protection | ❌ Not configured | GitHub repository | Configure in Settings |
| `daily` branch | ❌ Not created | GitHub repository | Create and push |

**⚠️ All other work is blocked until the GitHub repository is set up and the initial issues are created.**

---

## 🏁 Ready to Start?

Once the GitHub repository is set up and the repository is pushed:

1. **Create labels** (from `.github/LABELS.md`) in GitHub Settings
2. **Create milestones** (from `.github/PROJECT_PLAN.md`) in GitHub Issues
3. **Create M0 issues** (from `.github/PROJECT_PLAN.md`) using the templates
4. **Assign issues** to yourself or team members
5. **Setup branch protection** for `main` and `daily`
6. **Create `daily` branch** and push to GitHub
7. **Begin work** on M0-1: Setup GitHub Actions CI/CD workflows

---

## 📞 Need Help?

If you encounter any issues:

1. **Check the documentation**: All project rules are in `AGENTS.md`, `ASSISTANCE_IA.md`, and `docs/`

2. **Review the ADRs**: Architecture decisions are documented in `docs/decisions/`

3. **Check the contract**: The work contract is in `contrat/pack.py`

4. **Run the validation**: `python ci/valider_pack.py oeuvres/le-horla-maupassant-1887`

5. **Ask for clarification**: Use the issue templates to create a `needs-human` issue if something is unclear

---

## 📝 Cleanup Needed

The following files were created for GitLab and should be removed:

```bash
# To clean up GitLab-specific files:
rm -f .gitlab/PROJECT_PLAN.md .gitlab/ISSUE_TEMPLATES.md .gitlab/LABELS.md

# Then commit the cleanup:
git add -A
git commit -m "chore: remove GitLab-specific files, keep GitHub version"
```

---

*This document is a living guide. Update it as the project progresses on GitHub.*
