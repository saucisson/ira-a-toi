# GitHub Setup Script for "Ira à toi"

This script automates the creation of the GitHub repository, labels, milestones, and issues for the "Ira à toi" project.

---

## 🚀 Quick Start

### Method 1: Using the Setup Script (Recommended)

```bash
# Make the script executable
chmod +x scripts/setup_github.sh

# Run the script
./scripts/setup_github.sh
```

The script will:
1. Create the GitHub repository (or use existing)
2. Push all code and tags
3. Create all 47 labels
4. Create all 6 milestones (M0-M5)
5. Create all 12 M0 issues
6. Configure branch protection for `main` and `daily`
7. Create and push the `daily` branch

### Method 2: Manual Setup

If you prefer to do it manually, follow the steps below.

---

## 📋 What the Script Does

### 1. Repository Creation
- Creates a new GitHub repository named `ira-a-toi`
- Sets description: "Le nécessaire pour le dépôt - Collection 'Le Cabinet Noir'"
- Sets visibility to **private** (change in script if needed)
- Pushes all existing code and tags

### 2. Labels (47 total)
Creates labels in 5 categories:

#### Priority (3)
- `priority: high` - Critical, blocks other work
- `priority: medium` - Important feature
- `priority: low` - Nice to have

#### Category (13)
- `category: infrastructure` - CI/CD, Docker, tooling
- `category: content` - Literary works, fragments
- `category: frontend` - React, TypeScript, UI
- `category: backend` - Python, services, models
- `category: testing` - Tests, validation
- `category: documentation` - Docs, ADRs
- `category: validation` - Contract validation
- `category: design` - Interaction design
- `category: research` - Source finding
- `category: security` - Security tasks
- `category: agents` - Agent protocol
- `category: maintenance` - Updates, backups
- `category: ci` - Continuous Integration

#### Type (5)
- `type: feature` - New feature
- `type: bug` - Bug fix
- `type: chore` - Maintenance
- `type: refactor` - Code refactoring
- `type: documentation` - Documentation

#### Work-Specific (9)
- `work: le-horla` - Le Horla by Maupassant
- `work: second-oeuvre` - Second work
- `work: third-oeuvre` - Third work
- `contract` - Contract schema
- `cadence` - Cadence/pacing
- `ui` - User interface
- `interactions` - Micro-interactions
- `assets` - Assets (images, fonts)

#### Process (10)
- `needs-human` - Requires human decision
- `blocked` - Blocked by dependency
- `escalation` - Escalated to human
- `review` - Needs review
- `wip` - Work in progress
- `ready` - Ready for work
- `duplicate` - Duplicate issue
- `won't fix` - Won't be fixed
- `good first issue` - Beginner-friendly

#### Agent-Specific (7)
- `agent: developer` - Developer agent task
- `agent: reviewer` - Reviewer agent task
- `reviewer: blocking` - BLOCKING finding
- `reviewer: to-fix` - TO-FIX finding
- `reviewer: suggestion` - SUGGESTION finding
- `attempt: 1` - First attempt
- `attempt: 2` - Second attempt
- `attempt: 3` - Third attempt

### 3. Milestones (6 total)
- **M0: Project Infrastructure & Validation** (Due: +14 days)
- **M1: Complete Le Horla Pack** (Due: +42 days)
- **M2: First Additional Work** (Due: +63 days)
- **M3: Frontend Integration** (Due: +98 days)
- **M4: Production Deployment** (Due: +112 days)
- **M5: Monitoring & Maintenance** (Due: +126 days)

### 4. Issues (12 M0 issues)
Creates all 12 issues from M0 milestone with:
- Proper titles and descriptions
- Acceptance criteria
- Related documentation links
- Estimated effort
- Labels
- Milestone assignment

### 5. Branch Protection
Configures protection for:
- **main**: No direct pushes, CI checks required, administrators included
- **daily**: No direct pushes, CI checks required, administrators included

### 6. Daily Branch
Creates and pushes the `daily` branch as per ADR-0010.

---

## ⚙️ Customization

### Change Repository Settings
Edit the script to change:

```bash
REPO_NAME="ira-a-toi"
REPO_DESCRIPTION="Le nécessaire pour le dépôt - Collection 'Le Cabinet Noir'"
REPO_VISIBILITY="private"  # Change to "public" if needed
ORG_NAME=""  # Set to your org name if creating in an organization
```

### Change Due Dates
Edit the milestone creation section to change due dates:

```bash
due_on="$(date -d "+14 days" +%Y-%m-%dT00:00:00Z)"  # M0 due date
```

---

## 📝 Prerequisites

### 1. GitHub CLI (`gh`)
The script requires the GitHub CLI tool.

**Installation**:
- macOS: `brew install gh`
- Linux: `sudo apt install gh` (or use package manager)
- Windows: `winget install --id GitHub.cli`

**Authentication**:
```bash
gh auth login
```

Select:
- GitHub.com
- SSH protocol (recommended)
- Yes to authenticate

### 2. Git
Ensure Git is installed and configured with your SSH keys.

**Test SSH connection**:
```bash
ssh -T git@github.com
```

### 3. Repository State
The script assumes you are in the `ira-a-toi` project directory and have:
- All code committed to the `main` branch
- No uncommitted changes

---

## 🔧 Troubleshooting

### Error: "gh: command not found"
**Solution**: Install GitHub CLI as described above.

### Error: "Not authenticated with GitHub"
**Solution**: Run `gh auth login` and authenticate.

### Error: "Repository already exists"
**Solution**: The script handles this gracefully. It will use the existing repository.

### Error: "Label already exists"
**Solution**: The script will fail on duplicate labels. Run the script once, or delete existing labels first.

### Error: "Milestone already exists"
**Solution**: The script will fail on duplicate milestones. Delete existing milestones first.

### Error: Branch protection already exists
**Solution**: Update the existing protection rules manually in GitHub Settings.

### Script fails midway
**Solution**: 
1. Check which step failed
2. Manually complete that step
3. Re-run the script (it will skip already completed steps)

---

## 📚 Manual Setup Instructions

If you prefer not to use the script, here are the manual steps:

### 1. Create Repository
```bash
# On GitHub website:
# - Go to https://github.com/new
# - Repository name: ira-a-toi
# - Description: Le nécessaire pour le dépôt - Collection 'Le Cabinet Noir'
# - Visibility: Private
# - Don't initialize with README, .gitignore, or license

# Or via CLI:
gh repo create ira-a-toi --description "Le nécessaire pour le dépôt - Collection 'Le Cabinet Noir'" --private --push --source . --confirm
```

### 2. Push Code
```bash
git remote add origin git@github.com:<your-username>/ira-a-toi.git
git push -u origin main
git push --tags origin
```

### 3. Create Labels
Use the `gh` CLI for each label:
```bash
gh label create "priority: high" --color D73A4A --description "High priority - critical, blocks other work"
```

Or use the GitHub UI:
- Settings → Issues → Labels → New label

**See**: `.github/LABELS.md` for all 47 labels with colors and descriptions.

### 4. Create Milestones
Use the `gh` CLI:
```bash
gh api repos/<your-username>/ira-a-toi/milestones --method POST --field title="M0: Project Infrastructure & Validation" --field description="Ensure the template, CI/CD, and contract validation are fully operational." --field state="open"
```

Or use the GitHub UI:
- Issues → Milestones → New milestone

**See**: `.github/PROJECT_PLAN.md` for all 6 milestones.

### 5. Create Issues
Use the `gh` CLI:
```bash
gh issue create --title "M0-1: Setup GitHub Actions CI/CD workflows" --body "..." --label "priority: high,category: infrastructure,type: chore" --milestone "M0: Project Infrastructure & Validation"
```

Or use the GitHub UI:
- Issues → New issue

**See**: `.github/PROJECT_PLAN.md` for all 12 M0 issues with full descriptions.

### 6. Configure Branch Protection
GitHub UI:
- Settings → Branches → Branch protection rules → Add rule
- Branch name pattern: `main`
- Require a pull request before merging: ✅
- Require status checks: ✅ (select `check` and `web`)
- Include administrators: ✅
- Restrict who can push: ✅ (no one)

Repeat for `daily` branch.

### 7. Create Daily Branch
```bash
git checkout -b daily
git push origin daily
```

---

## 🎯 Verification

After running the script, verify everything was created:

### Check Labels
```bash
gh label list --repo <your-username>/ira-a-toi
```

### Check Milestones
```bash
gh api repos/<your-username>/ira-a-toi/milestones
```

### Check Issues
```bash
gh issue list --repo <your-username>/ira-a-toi --milestone "M0: Project Infrastructure & Validation"
```

### Check Branch Protection
GitHub UI: Settings → Branches

---

## 📖 References

- [GitHub CLI Documentation](https://cli.github.com/)
- [GitHub Labels API](https://docs.github.com/en/rest/issues/labels)
- [GitHub Milestones API](https://docs.github.com/en/rest/issues/milestones)
- [GitHub Issues API](https://docs.github.com/en/rest/issues/issues)
- [Project Documentation](../.github/PROJECT_PLAN.md)
- [Label Configuration](../.github/LABELS.md)

---

## 💡 Tips

1. **Run the script from the project root**:
   ```bash
   cd /home/alban/ira-a-toi
   ./scripts/setup_github.sh
   ```

2. **Make it executable first**:
   ```bash
   chmod +x scripts/setup_github.sh
   ```

3. **Review before running**:
   ```bash
   less scripts/setup_github.sh
   ```

4. **If it fails**, check the error message and refer to the troubleshooting section.

5. **After setup**, verify everything in the GitHub UI.

---

## ✅ Success Criteria

The setup is complete when:
- [ ] Repository exists on GitHub
- [ ] All 47 labels are created
- [ ] All 6 milestones are created
- [ ] All 12 M0 issues are created
- [ ] Branch protection is configured for `main` and `daily`
- [ ] `daily` branch exists and is pushed
- [ ] All code and tags are pushed to GitHub

---

*For more information, see the [main NEXT_STEPS.md](../NEXT_STEPS.md) file.*
