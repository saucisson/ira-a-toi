# GitHub Issue Templates for "Ira à toi"

This document provides **ready-to-use templates** for creating issues in **GitHub**.
Copy and paste these into GitHub's issue creation form.

---

## 📌 How to Use These Templates

1. **In GitHub UI**:
   - Go to **Issues → New Issue**
   - Click **"Get started"** and select a template, OR
   - Click **"Open blank issue"** and copy-paste the template below

2. **Fill in all sections** with relevant information

3. **Add appropriate labels** from the LABELS.md guide

4. **Assign to milestone** if applicable

5. **Set assignees** if you know who should work on it

---

## 📝 Task Issue Template

**Use for**: Standard development tasks (features, refactors, chores)

```markdown
## 📝 Description

<!-- Clear, concise description of what needs to be done -->

## 🎯 Acceptance Criteria

- [ ] 
- [ ] 
- [ ] 

## 📌 Related

- **Milestone**: [M0/M1/M2/M3/M4/M5]
- **Parent Issue**: #
- **Blocks**: #
- **Blocked by**: #
- **Related ADR**: [Link to ADR in docs/decisions/]

## 🏷️ Labels

<!-- Suggested labels - remove or add as needed -->
- `priority: high` / `priority: medium` / `priority: low`
- `category: infrastructure` / `category: content` / `category: frontend` / etc.
- `type: feature` / `type: chore` / `type: refactor` / etc.
- Work-specific labels (e.g., `work: le-horla`)

## ⚡ Estimated Effort

<!-- Time estimate in hours or days -->

## 📚 References

- [Link to relevant documentation]
- [Link to source material (Gallica/Wikisource URL)]
```

---

## 🐛 Bug Report Template

**Use for**: Reporting bugs or unexpected behavior

```markdown
## 🐛 Bug Description

<!-- What happened? What was expected? -->

### Steps to Reproduce

1. 
2. 
3. 

### Expected Behavior

### Actual Behavior

### Screenshots/Logs

```
<!-- Paste relevant logs or error messages -->
```

## 🔍 Investigation

- **Environment**: [Local/CI/Production/Docker]
- **Browser/OS**: [if frontend issue - e.g., Chrome v120, macOS 14]
- **Python version**: [if backend issue - e.g., Python 3.15.0]
- **Node.js version**: [if frontend issue]
- **Reproducible**: [Always/Sometimes/Random/Cannot reproduce]

## 🎯 Acceptance Criteria

- [ ] Bug root cause identified
- [ ] Bug fix implemented
- [ ] Regression test added
- [ ] CI passes
- [ ] Fix verified by human

## 📌 Related

- **Milestone**: 
- **Priority**: `priority: high` (for critical bugs)
- **Labels**: `type: bug`, `category: *`
- **Blocked issues**: #
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
- **Source URL**: [Wikisource/Gallica URL]
- **Domain Public Proof**: [Creator death year, source verification]

## 📝 Tasks

- [ ] Source complete text from original
- [ ] Verify domain public status (creator died +70 years ago)
- [ ] Create `manifeste.json` with proper metadata
- [ ] Split text into fragments in `fragments.json`
- [ ] Design micro-interactions (corruptions, choices, writings, find)
- [ ] Create cadences in `publication.json`
- [ ] Create enrichissements in `enrichissements.json`
- [ ] Validate with CI: `python ci/valider_pack.py oeuvres/<slug>`
- [ ] Add negative tests for new invariants
- [ ] Document all IA-generated content (genere_par_ia: true + valide_par)

## 🎯 Acceptance Criteria

- [ ] All text sourced from original (no rewriting)
- [ ] Domain public proof documented in pack
- [ ] CI validation passes (7 sections)
- [ ] All invariants respected
- [ ] No anti-altération errors
- [ ] All references (gestes, fins, enrichissements) point to existing objects

## 📌 Related

- **Milestone**: M1 or M2
- **Priority**: `priority: high`
- **Labels**: `category: content`, `work: *`

## 📚 Source Verification

| Item | Status | Source | Verification Date | Notes |
|------|--------|--------|-------------------|-------|
| Author death year | [✓/✗] | [Source] | [Date] | |
| Text source | [✓/✗] | [Wikisource/Gallica URL] | [Date] | |
| Illustrations | [✓/✗] | [Source] | [Date] | |
| Other assets | [✓/✗] | [Source] | [Date] | |

## 💡 Design Notes

<!-- Describe planned micro-interactions, cadences, etc. -->
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

### Must have
- [ ] 

### Should have
- [ ] 

### Nice to have
- [ ] 

## 🎯 Acceptance Criteria

- [ ] Feature implemented according to specification
- [ ] Unit tests added (90%+ coverage)
- [ ] Integration tests added (if applicable)
- [ ] Documentation updated
- [ ] CI passes
- [ ] Manual testing passed

## 📌 Related

- **Milestone**: 
- **Priority**: 
- **Labels**: `type: feature`, `category: *`
- **Related issues**: #

## 💡 Technical Notes

<!-- Additional context, constraints, or implementation ideas -->
```

---

## 🚨 Escalation Template

**Use for**: Issues requiring human decision (per ADR-0011 - Agent Protocol)

```markdown
## 🚨 ESCALATION REQUIRED

**Severity**: [question/urgent]

## ❓ Decision Needed

<!-- Clearly state the question or decision that requires human input -->

## 📋 Context

- **Related to**: [Issue #, Milestone, ADR, File]
- **Why escalation is needed**: [Explain why this cannot be decided autonomously per AGENTS.md §Escalation list]
- **Impact**: [What work is blocked? What are the consequences?]

## 🔍 Options

### Option 1: [Description]
- **Pros**: 
- **Cons**: 
- **Impact**: 

### Option 2: [Description]
- **Pros**: 
- **Cons**: 
- **Impact**: 

### Option 3: [Description]
- **Pros**: 
- **Cons**: 
- **Impact**: 

## 📌 Related

- **Blocked issues**: #
- **Dependencies**: #
- **Deadline**: [If applicable]

## 🏷️ Labels

**MUST include**:
- `needs-human`
- `escalation`

**Recommended**:
- `priority: high` (if urgent)
- Category label (e.g., `category: architecture`)

## ⏰ Timeline

- **Blocked since**: [Date]
- **Affects milestone**: [M0/M1/M2/M3/M4/M5]
- **Estimated delay**: [X hours/days if not resolved]
```

---

## 🔄 Refactor Template

**Use for**: Code refactoring or cleanup

```markdown
## 🔄 Refactor Description

<!-- What is being refactored? Why? -->

## 🎯 Goals

- [ ] Improve code readability
- [ ] Reduce cyclomatic complexity (target: ≤ 10)
- [ ] Fix technical debt
- [ ] Improve performance
- [ ] Better separation of concerns
- [ ] Other: 

## 📊 Current State

<!-- Describe current implementation and its issues -->
- **Location**: [File(s) or module(s)]
- **Current complexity**: [If known]
- **Issues**: 

## 🎯 Proposed Changes

<!-- Describe the refactoring approach -->

## ⚠️ Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Breaking existing functionality | | | Add regression tests |
| Performance regression | | | Benchmark before/after |
| Other dependencies affected | | | Check all call sites |

## 🎯 Acceptance Criteria

- [ ] Refactoring complete
- [ ] All existing tests pass
- [ ] New tests added for changed behavior
- [ ] No regression in functionality
- [ ] Code review passed
- [ ] Performance not degraded
- [ ] Onion architecture respected (if backend)

## 📌 Related

- **Milestone**: 
- **Priority**: 
- **Labels**: `type: refactor`, `category: *`
- **Related ADR**: [If this implements an ADR]
```

---

## 📚 Documentation Template

**Use for**: Documentation improvements

```markdown
## 📚 Documentation Task

**Type**: [New/Update/Review/Translate]

## 📝 Content to Document

<!-- What needs to be documented? -->

## 🎯 Target Audience

- [ ] Developers
- [ ] Designers
- [ ] Coding Agents
- [ ] Reviewer Agents
- [ ] End Users/Readers

## 📁 Location

- **File**: [Path to file]
- **Section**: [If updating existing doc]
- **New file**: [If creating new]

## 🎯 Acceptance Criteria

- [ ] Documentation written/updated
- [ ] Reviewed by at least one human
- [ ] Linked from relevant places (README, other docs)
- [ ] Up to date with current code
- [ ] Follows project style (no abbreviations, etc.)
- [ ] Examples included (if applicable)

## 📌 Related

- **Milestone**: 
- **Priority**: 
- **Labels**: `type: documentation`, `category: documentation`
- **Related code/files**: 

## 💡 Notes

<!-- Additional context or requirements -->
```

---

## 🎨 Design Template

**Use for**: UI/UX design tasks or narrative design

```markdown
## 🎨 Design Task

**Type**: [UI/UX/Narrative/Interaction]

## 📝 Description

<!-- What needs to be designed? -->

## 🎯 Objectives

- [ ] 
- [ ] 
- [ ] 

## 📐 Requirements

### Functional
- [ ] 

### Aesthetic
- [ ] Matches "Cabinet Noir" theme
- [ ] Respects typography skins (peau)
- [ ] Accessible (WCAG 2.1 AA)

### Technical
- [ ] Works on mobile, tablet, desktop
- [ ] Performance: [Target FPS/load time]

## 🎨 Design Assets

<!-- Links to mockups, wireframes, etc. -->
- 

## 📊 User Flow

```
<!-- Describe the user flow if applicable -->
```

## 🎯 Acceptance Criteria

- [ ] Design approved by narrative designer
- [ ] Technical feasibility confirmed
- [ ] Implemented according to spec
- [ ] Tested on all target devices
- [ ] Accessibility audit passed

## 📌 Related

- **Milestone**: 
- **Priority**: 
- **Labels**: `category: design`, `type: feature`
- **Related issues**: #
```

---

## 🔒 Security Template

**Use for**: Security-related tasks or vulnerabilities

```markdown
## 🔒 Security Issue

**Severity**: [critical/high/medium/low]

## 📝 Description

<!-- Describe the security issue -->

## ⚠️ Impact

- **Affected components**: 
- **Potential damage**: 
- **Exploitability**: [Easy/Moderate/Difficult]

## 🎯 Reproduction

```
<!-- Steps to reproduce if applicable -->
```

## 🔍 Investigation

- **Discovered by**: [Manual/Audit/Scan/Report]
- **Discovered on**: [Date]
- **Reported by**: [If applicable]

## 🛡️ Mitigation

### Immediate (if needed)
- [ ] 

### Long-term
- [ ] 

## 🎯 Acceptance Criteria

- [ ] Vulnerability fixed
- [ ] No new vulnerabilities introduced
- [ ] Security tests added
- [ ] Incident documented
- [ ] All secrets rotated (if applicable)
- [ ] Security audit passed

## 📌 Related

- **Milestone**: 
- **Priority**: `priority: high` (or `priority: medium` if low severity)
- **Labels**: `category: security`, `type: bug`
- **Blocked**: All deployments until resolved (if critical)
```

---

## 📊 Label Cheat Sheet

### Priority (Pick ONE)
- `priority: high` - Critical, blocks other work
- `priority: medium` - Important, should be done soon
- `priority: low` - Nice to have, backlog

### Category (Pick ONE or MORE)
- `category: infrastructure` - CI/CD, Docker, tooling, servers
- `category: content` - Literary works, fragments, enrichissements
- `category: frontend` - React, TypeScript, UI/UX
- `category: backend` - Python, services, models
- `category: testing` - Tests, validation, CI tests
- `category: documentation` - Docs, ADRs, guides
- `category: validation` - Contract validation, CI checks
- `category: design` - Interaction design, UX, visual design
- `category: research` - Source finding, domain public verification
- `category: security` - Security, secrets, audits
- `category: agents` - Agent protocol, reviewer, notifications
- `category: maintenance` - Updates, backups, monitoring

### Type (Pick ONE)
- `type: feature` - New functionality
- `type: bug` - Bug fix
- `type: chore` - Maintenance task
- `type: refactor` - Code improvement
- `type: documentation` - Documentation work

### Work-specific (Pick as needed)
- `work: le-horla` - Maupassant's Le Horla
- `work: second-oeuvre` - Second literary work
- `contract` - Contract schema work
- `cadence` - Cadence/pacing work
- `ui` - User interface work
- `interactions` - Micro-interactions work
- `assets` - Asset creation/collection

### Process (Pick as needed)
- `needs-human` - Requires human decision
- `blocked` - Blocked by another issue
- `escalation` - Escalated to human
- `review` - Needs code/design review
- `wip` - Work in progress
- `ready` - Ready for work

---

## 🎯 Priority Guidelines

| Priority | When to Use | SLA |
|----------|--------------|-----|
| `priority: high` | Blocks other work, critical bug, production issue | Address within 1-2 days |
| `priority: medium` | Important feature, milestone deliverable | Address within 1-2 weeks |
| `priority: low` | Nice-to-have, backlog item | Address when resources allow |

---

## 📌 Template Selection Guide

| Situation | Recommended Template |
|-----------|----------------------|
| Standard development task | Task Issue Template |
| Bug found | Bug Report Template |
| New literary work | Content Creation Template |
| New feature request | Feature Request Template |
| Need human decision | Escalation Template |
| Code improvement | Refactor Template |
| Documentation needed | Documentation Template |
| UI/UX design | Design Template |
| Security issue | Security Template |

---

*These templates follow the project's constitutional documents and ADR-0011 (Agent Protocol).*
