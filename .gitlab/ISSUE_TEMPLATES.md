# GitLab Issue Templates for "Ira à toi"

This document provides **ready-to-use templates** for creating issues in GitLab.
Copy and paste these into GitLab's issue creation form.

---

## 📌 Task Issue Template

**Use for**: Standard development tasks (features, refactors, chores)

```markdown
## 📝 Description

<!-- Clear, concise description of what needs to be done -->

## 🎯 Acceptance Criteria

- [ ] Criteria 1
- [ ] Criteria 2
- [ ] Criteria 3

## 📌 Related

- **Milestone**: [M0/M1/M2/M3/M4/M5]
- **Parent Issue**: #xxx (if applicable)
- **Blocks**: #xxx (if this blocks other issues)
- **Blocked by**: #xxx (if this is blocked by other issues)

## 🏷️ Labels

<!-- Add appropriate labels -->
- `priority:high` / `priority:medium` / `priority:low`
- `category:infrastructure` / `category:content` / `category:frontend` / etc.
- `type:feature` / `type:chore` / `type:refactor` / etc.
- Work-specific labels (e.g., `work:le-horla`)

## ⚡ Estimated Effort

<!-- Time estimate in hours or days -->

## 📚 References

- [Link to relevant documentation]
- [Link to related ADR]
- [Source material (Gallica/Wikisource URL)]
```

---

## 🐛 Bug Report Template

**Use for**: Reporting bugs or unexpected behavior

```markdown
## 🐛 Bug Description

<!-- What happened? What was expected? -->

### Steps to Reproduce

1. Step 1
2. Step 2
3. Step 3

### Expected Behavior

### Actual Behavior

### Screenshots/Logs

```
<!-- Paste relevant logs or error messages -->
```

## 🔍 Investigation

- **Environment**: [Local/CI/Production]
- **Browser/OS**: [if frontend issue]
- **Python version**: [if backend issue]
- **Reproducible**: [Always/Sometimes/Random]

## 🎯 Acceptance Criteria

- [ ] Bug is fixed
- [ ] Regression test added
- [ ] CI passes

## 📌 Related

- **Milestone**: 
- **Priority**: `priority:high` (for critical bugs)
- **Labels**: `type:bug`, `category:*`
```

---

## 📖 Content Creation Template

**Use for**: Creating new literary works or enriching existing ones

```markdown
## 📖 Work Information

- **Title**: 
- **Author**: 
- **Year**: 
- **Line**: [cabinet-fantastique/correspondances/feuilleton]
- **Source**: [Wikisource/Gallica URL]
- **Domain Public Proof**: [Creator death year, source verification]

## 📝 Tasks

- [ ] Source complete text
- [ ] Verify domain public status
- [ ] Create manifeste.json
- [ ] Split text into fragments
- [ ] Design micro-interactions (corruptions, choices, writings, find)
- [ ] Create cadences
- [ ] Create enrichissements
- [ ] Validate with CI
- [ ] Add negative tests

## 🎯 Acceptance Criteria

- [ ] All text sourced from original
- [ ] Domain public proof documented
- [ ] CI validation passes
- [ ] All invariants respected

## 📌 Related

- **Milestone**: M1 or M2
- **Priority**: `priority:high`
- **Labels**: `category:content`, `work:*`

## 📚 Source Verification

| Item | Status | Source | Verification |
|------|--------|--------|--------------|
| Author death year | | | |
| Text source | | | |
| Illustrations | | | |
| Other assets | | | |
```

---

## ✨ Feature Request Template

**Use for**: Requesting new features or enhancements

```markdown
## ✨ Feature Description

<!-- What feature are you requesting? Why is it needed? -->

## 🎯 User Value

<!-- How does this benefit the reader/player? -->

## 📋 Requirements

- **Must have**: 
- **Should have**: 
- **Nice to have**: 

## 🎯 Acceptance Criteria

- [ ] Feature implemented
- [ ] Tests added
- [ ] Documentation updated
- [ ] CI passes

## 📌 Related

- **Milestone**: 
- **Priority**: 
- **Labels**: `type:feature`, `category:*`

## 💡 Notes

<!-- Additional context or constraints -->
```

---

## 🚨 Escalation Template

**Use for**: Issues requiring human decision (per ADR-0011)

```markdown
## 🚨 ESCALATION REQUIRED

**Severity**: [question/urgent]

## ❓ Question

<!-- Clearly state the question or decision needed -->

## 📋 Options

1. **Option A**: 
   - Pros: 
   - Cons: 

2. **Option B**: 
   - Pros: 
   - Cons: 

## 📌 Context

- **Related to**: [Issue #, Milestone, ADR]
- **Why escalation is needed**: [Explain why this cannot be decided autonomously]
- **Blocked work**: [What work is blocked by this?]

## 🏷️ Labels

- `needs-human`
- `priority:high` (if urgent)
- `escalation`

## ⏰ Timeline Impact

- **Blocked since**: [Date]
- **Affects milestone**: [M0/M1/M2/M3/M4/M5]
```

---

## 🔄 Refactor Template

**Use for**: Code refactoring or cleanup

```markdown
## 🔄 Refactor Description

<!-- What is being refactored? Why? -->

## 🎯 Goals

- [ ] Improve readability
- [ ] Reduce complexity
- [ ] Fix technical debt
- [ ] Improve performance
- [ ] Other: 

## 📊 Current State

<!-- Describe current implementation and its issues -->

## 🎯 Acceptance Criteria

- [ ] Refactoring complete
- [ ] All tests pass
- [ ] No regression in functionality
- [ ] Code review passed

## ⚠️ Risks

- **Breaking changes**: [Yes/No]
- **Migration needed**: [Yes/No]
- **Dependencies**: 

## 📌 Related

- **Milestone**: 
- **Priority**: 
- **Labels**: `type:refactor`, `category:*`
```

---

## 📚 Documentation Template

**Use for**: Documentation improvements

```markdown
## 📚 Documentation Task

**Type**: [New/Update/Review]

## 📝 Content

<!-- What needs to be documented? -->

## 🎯 Target Audience

- [ ] Developers
- [ ] Designers
- [ ] Agents
- [ ] Users/Readers

## 📁 Location

- **File**: 
- **Section**: 

## 🎯 Acceptance Criteria

- [ ] Documentation written
- [ ] Reviewed by team
- [ ] Linked from relevant places
- [ ] Up to date with code

## 📌 Related

- **Milestone**: 
- **Priority**: 
- **Labels**: `type:documentation`, `category:documentation`
```

---

## Usage Instructions

1. **Choose the appropriate template** based on the issue type
2. **Copy the template** into the GitLab issue creation form
3. **Fill in all sections** with relevant information
4. **Add appropriate labels** from the labels list
5. **Assign to milestone** if applicable
6. **Set priority** appropriately

---

## Label Cheat Sheet

### Priority (Pick ONE)
- `priority:high` - Critical, blocks other work
- `priority:medium` - Important, should be done soon
- `priority:low` - Nice to have, backlog

### Category (Pick ONE or MORE)
- `category:infrastructure` - CI/CD, Docker, tooling
- `category:content` - Literary works, fragments, enrichissements
- `category:frontend` - React, TypeScript, UI
- `category:backend` - Python, services, models
- `category:testing` - Tests, validation, CI
- `category:documentation` - Docs, ADRs, guides
- `category:validation` - Contract validation, CI checks
- `category:design` - Interaction design, UX
- `category:research` - Source finding, domain public verification
- `category:security` - Security, secrets, audits
- `category:agents` - Agent protocol, reviewer
- `category:maintenance` - Updates, backups, monitoring

### Type (Pick ONE)
- `type:feature` - New functionality
- `type:bug` - Bug fix
- `type:chore` - Maintenance task
- `type:refactor` - Code improvement
- `type:documentation` - Documentation work

### Work-specific (Pick as needed)
- `work:le-horla` - Maupassant's Le Horla
- `work:second-oeuvre` - Second literary work
- `contract` - Contract schema work
- `cadence` - Cadence/pacing work
- `ui` - User interface work
- `interactions` - Micro-interactions work
- `assets` - Asset creation/collection

---

## Priority Guidelines

| Priority | When to Use | SLA |
|----------|--------------|-----|
| `priority:high` | Blocks other work, critical bug, production issue | Address within 1-2 days |
| `priority:medium` | Important feature, milestone deliverable | Address within 1-2 weeks |
| `priority:low` | Nice-to-have, backlog item | Address when resources allow |

---

## Milestone Mapping

| Milestone | Focus | Target Completion |
|-----------|-------|-------------------|
| M0 | Infrastructure & Validation | Sprint 1 |
| M1 | Complete Le Horla Pack | Sprint 2-3 |
| M2 | First Additional Work | Sprint 4 |
| M3 | Frontend Integration | Sprint 5-6 |
| M4 | Production Deployment | Sprint 7 |
| M5 | Monitoring & Maintenance | Sprint 8 |
