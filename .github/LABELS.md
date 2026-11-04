# GitHub Labels Configuration for "Ira à toi"

> **Platform**: GitHub (not GitLab)
> **Purpose**: Standardize issue and pull request labeling

---

## 📌 Quick Start

### To create these labels in GitHub:

1. Go to **Your Repository → Settings → Issues → Labels → New label**
2. Enter the **Label name** (exact match required)
3. Select the **Color** (use the hex codes provided)
4. Add a **Description** (optional but recommended)
5. Click **Create label**

### Bulk creation option:
Use the GitHub API or a script to create all labels at once. See the [GitHub API documentation](https://docs.github.com/en/rest/issues/labels#create-a-label) for details.

---

## 🏷️ Label Categories

---

## 1. Priority Labels

**Purpose**: Indicate the urgency/importance of an issue

| Name | Color (Hex) | GitHub Color Name | Description | When to Use |
|------|-------------|-------------------|-------------|-------------|
| `priority: high` | `#D73A4A` | Red | High priority - critical, blocks other work | Critical bugs, milestone blockers, production issues |
| `priority: medium` | `#FBCA04` | Yellow | Medium priority - important feature | Milestone deliverables, important improvements |
| `priority: low` | `#0E8A16` | Green | Low priority - nice to have | Backlog items, minor improvements, enhancements |

**Rule**: Exactly ONE priority label per issue

---

## 2. Category Labels

**Purpose**: Categorize the type of work

| Name | Color (Hex) | Color | Description |
|------|-------------|-------|-------------|
| `category: infrastructure` | `#6F42C1` | Purple | Infrastructure-related tasks | CI/CD, Docker, tooling, servers, deployment |
| `category: content` | `#1D76DB` | Blue | Literary content tasks | Works, fragments, enrichissements, source texts |
| `category: frontend` | `#006B75` | Teal | Frontend development | React, TypeScript, UI, components, styling |
| `category: backend` | `#000000` | Black | Backend development | Python, services, models, contract |
| `category: testing` | `#E66600` | Dark Orange | Testing-related tasks | Unit tests, integration tests, test coverage |
| `category: documentation` | `#5319E7` | Violet | Documentation tasks | Docs, ADRs, guides, READMEs |
| `category: validation` | `#11E109` | Light Green | Validation tasks | Contract validation, CI checks, quality gates |
| `category: design` | `#FF77CC` | Pink | Design tasks | Interaction design, UX, visual design |
| `category: research` | `#7C3AED` | Dark Violet | Research tasks | Source finding, domain public verification |
| `category: security` | `#D93F0B` | Dark Red | Security tasks | Security audits, vulnerability fixes, secrets |
| `category: agents` | `#F98400` | Dark Orange | Agent-related tasks | Agent protocol, reviewer, notifications |
| `category: maintenance` | `#576474` | Gray | Maintenance tasks | Updates, backups, monitoring, dependencies |

**Rule**: At least ONE category label per issue. Multiple allowed if applicable.

---

## 3. Type Labels

**Purpose**: Indicate the nature of the work

| Name | Color (Hex) | Color | Description |
|------|-------------|-------|-------------|
| `type: feature` | `#1D76DB` | Blue | New feature development | Adding new functionality |
| `type: bug` | `#D73A4A` | Red | Bug fix | Fixing defects, issues, or errors |
| `type: chore` | `#576474` | Gray | Maintenance chore | Routine maintenance, cleanup |
| `type: refactor` | `#6F42C1` | Purple | Code refactoring | Improving existing code structure |
| `type: documentation` | `#5319E7` | Violet | Documentation work | Writing or updating documentation |

**Rule**: Exactly ONE type label per issue

---

## 4. Work-Specific Labels

**Purpose**: Track work on specific literary works or components

| Name | Color (Hex) | Color | Description |
|------|-------------|-------|-------------|
| `work: le-horla` | `#1D76DB` | Blue | Le Horla by Maupassant | Tasks related to the Le Horla pack |
| `work: second-oeuvre` | `#0E8A16` | Green | Second literary work | Tasks for the second work in the collection |
| `work: third-oeuvre` | `#6F42C1` | Purple | Third literary work | Tasks for the third work |
| `contract` | `#E66600` | Dark Orange | Contract schema | Tasks related to the work contract (pack.py) |
| `cadence` | `#6F42C1` | Purple | Cadence/pacing | Tasks related to scheduling and pacing |
| `ui` | `#006B75` | Teal | User interface | UI-specific tasks |
| `interactions` | `#F98400` | Dark Orange | Micro-interactions | Tasks for gestures, states, conditions |
| `assets` | `#11E109` | Light Green | Assets | Tasks for images, fonts, audio files |
| `ci` | `#E66600` | Dark Orange | Continuous Integration | CI-specific tasks |

**Rule**: Use as needed. Multiple can be applied if relevant.

---

## 5. Process/Workflow Labels

**Purpose**: Track the status of issues in the workflow

| Name | Color (Hex) | Color | Description |
|------|-------------|-------|-------------|
| `needs-human` | `#D73A4A` | Red | Requires human decision | Per ADR-0011, escalation needed. **CRITICAL**: All work stops if this label appears with `urgent` severity |
| `blocked` | `#D93F0B` | Dark Red | Blocked by dependency | Work cannot proceed due to another issue or dependency |
| `escalation` | `#E66600` | Dark Orange | Escalated to human | Issue has been escalated per ADR-0011 |
| `review` | `#FBCA04` | Yellow | Needs review | Requires code/design review before merging |
| `wip` | `#576474` | Gray | Work in progress | Currently being worked on |
| `ready` | `#0E8A16` | Green | Ready for work | Approved and ready to be picked up |
| `duplicate` | `#576474` | Gray | Duplicate issue | This issue duplicates another issue |
| `won't fix` | `#576474` | Gray | Won't be fixed | Decision made not to address this issue |
| `good first issue` | `#0E8A16` | Green | Beginner-friendly | Good for new contributors |

**Rule**: Use to track workflow state. `needs-human` and `escalation` have special workflows per ADR-0011.

---

## 6. Agent-Specific Labels

**Purpose**: Labels specific to the agent protocol (ADR-0011)

| Name | Color (Hex) | Color | Description |
|------|-------------|-------|-------------|
| `agent: developer` | `#1D76DB` | Blue | Developer agent task | Task assigned to or for developer agent |
| `agent: reviewer` | `#7C3AED` | Dark Violet | Reviewer agent task | Task related to reviewer agent |
| `reviewer: blocking` | `#D73A4A` | Red | BLOCKING finding | Reviewer found a blocking issue |
| `reviewer: to-fix` | `#FBCA04` | Yellow | TO-FIX finding | Reviewer found an issue that should be fixed |
| `reviewer: suggestion` | `#0E8A16` | Green | SUGGESTION finding | Reviewer has a non-blocking suggestion |
| `attempt: 1` | `#576474` | Gray | First attempt | First attempt at this issue |
| `attempt: 2` | `#FBCA04` | Yellow | Second attempt | Second attempt at this issue |
| `attempt: 3` | `#D73A4A` | Red | Third attempt | Third and final attempt at this issue |
| `blocked` | `#D93F0B` | Dark Red | Blocked after 3 attempts | Issue blocked per ADR-0010 (3 attempts rule) |

---

## 🎨 Color Palette Summary

| Color Name | Hex Code | Usage |
|------------|----------|-------|
| **Reds** | | Critical/High Priority |
| Red | `#D73A4A` | priority: high, type: bug, needs-human |
| Dark Red | `#D93F0B` | blocked, category: security |
| **Oranges/Yellows** | | Medium Priority/Warnings |
| Yellow | `#FBCA04` | priority: medium, review |
| Dark Orange | `#E66600` | category: testing, category: agents, escalation, contract, interactions, ci |
| Orange | `#F98400` | work: second-oeuvre, type: chore |
| **Greens** | | Low Priority/Success |
| Green | `#0E8A16` | priority: low, type: documentation, work: le-horla, ready, good first issue |
| Light Green | `#11E109` | category: validation, assets |
| **Blues** | | Content/Features |
| Blue | `#1D76DB` | category: content, type: feature, work: le-horla |
| **Purples** | | Backend/Architecture |
| Purple | `#6F42C1` | category: backend, type: refactor, work: third-oeuvre, cadence, agent: reviewer |
| Dark Violet | `#7C3AED` | category: research, category: documentation, agent: reviewer |
| **Teals** | | Frontend |
| Teal | `#006B75` | category: frontend, ui |
| **Pinks** | | Design |
| Pink | `#FF77CC` | category: design |
| **Grays/Blacks** | | Maintenance/Process |
| Black | `#000000` | category: backend |
| Gray | `#576474` | category: maintenance, type: chore, wip, duplicate, won't fix, attempt: 1, attempt: 2, attempt: 3 |

---

## 📋 Label Creation Order

**Recommended order for creating labels**:

### Phase 1: Core Labels (Create First)
1. Priority labels (`priority: high`, `priority: medium`, `priority: low`)
2. Type labels (`type: feature`, `type: bug`, `type: chore`, `type: refactor`, `type: documentation`)
3. Basic category labels (`category: infrastructure`, `category: content`, `category: frontend`, `category: backend`)

### Phase 2: Process Labels
4. Process labels (`needs-human`, `blocked`, `escalation`, `review`, `wip`, `ready`)

### Phase 3: Work-Specific Labels
5. Work-specific labels (`work: le-horla`, `contract`, `cadence`, etc.)

### Phase 4: Remaining Categories
6. Remaining category labels

### Phase 5: Agent Labels
7. Agent-specific labels (create as needed)

---

## 🔍 Label Query Examples

Use these in GitHub's issue search:

### Find all high priority issues:
```
label:priority:high
```

### Find all Le Horla related issues:
```
label:work:le-horla
```

### Find all frontend bugs:
```
label:category:frontend label:type:bug
```

### Find all issues that need human decision:
```
label:needs-human
```

### Find all blocked issues:
```
label:blocked
```

### Find all issues for M0 milestone:
```
milestone:M0
```

### Find all content tasks:
```
label:category:content
```

### Find all issues assigned to current user:
```
assignee:@me
```

### Find all issues in current milestone:
```
milestone:M0 assignee:@me
```

---

## 📊 Label Statistics

| Category | Count | Purpose |
|----------|-------|---------|
| Priority | 3 | Indicate urgency |
| Category | 13 | Categorize work type |
| Type | 5 | Indicate work nature |
| Work-specific | 9 | Track specific works/components |
| Process | 8 | Track workflow state |
| Agent-specific | 9 | Agent protocol tracking |
| **Total** | **47** | All labels |

---

## 🎯 Label Usage Guidelines

### 1. Priority Labels
- **Exactly ONE** per issue
- Default: `priority: medium` if not specified
- Use `priority: high` sparingly (only for critical blockers)

### 2. Category Labels
- **At least ONE** per issue
- Multiple allowed if the issue spans categories
- Example: A frontend testing issue could have both `category: frontend` and `category: testing`

### 3. Type Labels
- **Exactly ONE** per issue
- Maps to Conventional Commits types:
  - `type: feature` → `feat:`
  - `type: bug` → `fix:`
  - `type: chore` → `chore:`
  - `type: refactor` → `refactor:`
  - `type: documentation` → `docs:`

### 4. Work-Specific Labels
- Use as needed to categorize work
- Multiple can be applied if relevant
- Create new work-specific labels as new works are added

### 5. Process Labels
- Use to track workflow state
- **Important**: `needs-human` and `escalation` have special workflows per ADR-0011
- When adding `needs-human`, also add `escalation` and set severity in the issue title/description

### 6. Agent Labels
- Used by agents to track their work
- `attempt: 1/2/3` tracks the 3-attempt rule from ADR-0010
- `reviewer: *` labels are used by the reviewer agent

---

## 🏷️ Default Label Sets

### For a New Feature Issue:
```
Labels: priority: medium, type: feature, category: *
```

### For a Bug Fix:
```
Labels: priority: high, type: bug, category: *
```

### For a Content Task:
```
Labels: priority: medium, type: feature, category: content, work: *
```

### For an Infrastructure Task:
```
Labels: priority: medium, type: chore, category: infrastructure
```

### For a Refactor:
```
Labels: priority: low, type: refactor, category: backend
```

### For a Documentation Task:
```
Labels: priority: low, type: documentation, category: documentation
```

### For an Escalation:
```
Labels: needs-human, escalation, priority: high, category: *
```

---

## 📝 Label Maintenance

### Adding New Labels
1. **Discuss** with the team if a new label is needed
2. **Check** if an existing label could be used instead
3. **Follow naming convention**: `category: *`, `type: *`, `work: *`, etc.
4. **Use appropriate color** from the palette
5. **Document** the new label in this file

### Archiving Labels
- GitHub doesn't have an "archive" function, but you can:
  - **Delete** the label if it's no longer needed
  - **Rename** it if the meaning changes
- Update this documentation when labels are changed

### Regular Review
- **Quarterly**: Review all labels for relevance
- **Merge similar** labels if they serve the same purpose
- **Remove unused** labels after confirming they're not needed
- **Update colors** if the palette needs adjustment

---

## 🔗 Related Documentation

- [AGENTS.md](../AGENTS.md) - Agent constitution and escalation rules
- [ASSISTANCE_IA.md](../ASSISTANCE_IA.md) - AI assistance rules
- [docs/branching.md](../docs/branching.md) - Branch model and day cycle
- [docs/agents/escalation.md](../docs/agents/escalation.md) - Escalation protocol
- [PROJECT_PLAN.md](./PROJECT_PLAN.md) - Milestones and issues
- [ISSUE_TEMPLATES.md](./ISSUE_TEMPLATES.md) - Issue templates

---

## 💡 Best Practices

1. **Be consistent**: Always use the same label names
2. **Be specific**: Use the most specific label that applies
3. **Don't over-label**: 3-5 labels per issue is usually enough
4. **Use priority wisely**: Most issues should be `priority: medium`
5. **Update labels**: Remove labels that no longer apply as work progresses
6. **Combine strategically**: Use label combinations to create powerful queries

---

## ✅ Verification Checklist

After creating all labels, verify:

- [ ] All priority labels exist (`priority: high`, `priority: medium`, `priority: low`)
- [ ] All type labels exist
- [ ] All category labels exist
- [ ] All process labels exist
- [ ] Colors match the specified hex codes
- [ ] Descriptions are clear and helpful
- [ ] This file is up to date with all created labels

---

*This configuration follows the project's constitutional documents (AGENTS.md, ASSISTANCE_IA.md) and ADR-0011 (Agent Protocol).*
