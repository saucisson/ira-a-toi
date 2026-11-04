# GitLab Labels Configuration for "Ira à toi"

This document defines all **labels** that should be created in GitLab for the "Ira à toi" project.

---

## 🎯 How to Create These Labels

### In GitLab UI:
1. Go to **Project → Settings → General → Labels**
2. Click **"New label"**
3. Fill in:
   - **Title**: The label name (e.g., `priority:high`)
   - **Color**: Use the suggested color or choose your own
   - **Description**: The description from below
4. Click **"Create label"**

### Via GitLab API:
```bash
curl --request POST \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --header "Content-Type: application/json" \
  --data '{"name": "priority:high", "color": "#ff0000", "description": "High priority - critical, blocks other work"}' \
  "https://gitlab.example.com/api/v4/projects/<project_id>/labels"
```

---

## 🏷️ Priority Labels

| Label | Color (Hex) | Color (Name) | Description | When to Use |
|-------|-------------|--------------|-------------|-------------|
| `priority:high` | `#ff0000` | Red | High priority - critical, blocks other work | Critical bugs, milestone blockers |
| `priority:medium` | `#ff9900` | Orange | Medium priority - important feature | Milestone deliverables, important improvements |
| `priority:low` | `#0066cc` | Blue | Low priority - nice to have | Backlog items, minor improvements |

---

## 📁 Category Labels

| Label | Color (Hex) | Color (Name) | Description |
|-------|-------------|--------------|-------------|
| `category:infrastructure` | `#663399` | Purple | Infrastructure-related tasks | CI/CD, Docker, tooling, servers |
| `category:content` | `#339966` | Green | Literary content tasks | Works, fragments, enrichissements |
| `category:frontend` | `#00cc99` | Teal | Frontend development | React, TypeScript, UI/UX |
| `category:backend` | `#666699` | Indigo | Backend development | Python, services, models |
| `category:testing` | `#cc3300` | Dark Orange | Testing-related tasks | Unit tests, integration tests, CI tests |
| `category:documentation` | `#996633` | Brown | Documentation tasks | Docs, ADRs, guides, READMEs |
| `category:validation` | `#33cc33` | Light Green | Validation tasks | Contract validation, CI checks, quality gates |
| `category:design` | `#ff6699` | Pink | Design tasks | Interaction design, UX, visual design |
| `category:research` | `#9933cc` | Violet | Research tasks | Source finding, domain public verification |
| `category:security` | `#cc0033` | Dark Red | Security tasks | Security audits, vulnerability fixes |
| `category:agents` | `#ffcc00` | Gold | Agent-related tasks | Agent protocol, reviewer, notifications |
| `category:maintenance` | `#666666` | Gray | Maintenance tasks | Updates, backups, monitoring |

---

## 🔧 Type Labels

| Label | Color (Hex) | Color (Name) | Description |
|-------|-------------|--------------|-------------|
| `type:feature` | `#0099cc` | Light Blue | New feature development | Adding new functionality |
| `type:bug` | `#cc0000` | Red | Bug fix | Fixing defects |
| `type:chore` | `#999999` | Gray | Maintenance chore | Routine maintenance tasks |
| `type:refactor` | `#663399` | Purple | Code refactoring | Improving existing code |
| `type:documentation` | `#339966` | Green | Documentation | Writing or updating docs |

---

## 📚 Work-Specific Labels

| Label | Color (Hex) | Color (Name) | Description |
|-------|-------------|--------------|-------------|
| `work:le-horla` | `#0066cc` | Blue | Le Horla by Maupassant | Tasks related to the Le Horla pack |
| `work:second-oeuvre` | `#009966` | Green | Second literary work | Tasks for the second work in the collection |
| `contract` | `#cc3300` | Orange | Contract schema | Tasks related to the work contract (pack.py) |
| `cadence` | `#663399` | Purple | Cadence/pacing | Tasks related to scheduling and pacing |
| `ui` | `#00cc99` | Teal | User interface | UI-specific tasks |
| `interactions` | `#ff6600` | Orange | Micro-interactions | Tasks for gestures, states, conditions |
| `assets` | `#3399cc` | Light Blue | Assets | Tasks for images, fonts, audio |

---

## 🏛️ Process Labels

| Label | Color (Hex) | Color (Name) | Description |
|-------|-------------|--------------|-------------|
| `needs-human` | `#ff0000` | Red | Requires human decision | Per ADR-0011, escalation needed |
| `blocked` | `#cc0000` | Dark Red | Blocked | Work cannot proceed due to dependency |
| `escalation` | `#ff6600` | Orange | Escalated issue | Issue has been escalated to human |
| `review` | `#ffcc00` | Gold | Needs review | Requires code/design review |
| `wip` | `#996633` | Brown | Work in progress | Currently being worked on |
| `ready` | `#33cc33` | Light Green | Ready for work | Approved and ready to be picked up |
| `duplicate` | `#666666` | Gray | Duplicate | Duplicate of another issue |

---

## 📊 Label Usage Guidelines

### Priority Labels
- **Exactly ONE** priority label per issue
- Default: `priority:medium` if not specified

### Category Labels
- **At least ONE** category label per issue
- Can have multiple if the issue spans categories
- Example: A frontend testing issue could have both `category:frontend` and `category:testing`

### Type Labels
- **Exactly ONE** type label per issue
- Use `type:feature` for new functionality
- Use `type:bug` for bug fixes
- Use `type:chore` for maintenance tasks
- Use `type:refactor` for code improvements
- Use `type:documentation` for documentation work

### Work-Specific Labels
- Use as needed to categorize work
- Multiple can be applied if relevant

### Process Labels
- Use to track workflow state
- `needs-human` and `escalation` are special - per ADR-0011
- `blocked` should include a comment explaining what it's blocked by

---

## 🎨 Color Palette Reference

| Color Name | Hex Code | Usage |
|------------|----------|-------|
| Red | `#ff0000` | High priority, bugs, critical |
| Orange | `#ff9900` | Medium priority, warnings |
| Yellow/Gold | `#ffcc00` | Agents, review |
| Light Green | `#33cc33` | Low priority, ready, validation |
| Dark Green | `#339966` | Content, documentation |
| Teal | `#00cc99` | Frontend, UI |
| Light Blue | `#0099cc` | Type: feature, work-specific |
| Blue | `#0066cc` | Low priority, work:le-horla |
| Purple | `#663399` | Infrastructure, refactor, cadence |
| Dark Purple | `#9933cc` | Research |
| Pink | `#ff6699` | Design |
| Brown | `#996633` | Documentation, WIP |
| Gray | `#666666` | Chore, maintenance, duplicate |
| Dark Gray | `#999999` | Type: chore |

---

## 🔍 Label Query Examples

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
label:category:frontend,type:bug
```

### Find all issues that need human decision:
```
label:needs-human
```

### Find all blocked issues:
```
label:blocked
```

### Find all content tasks:
```
label:category:content
```

---

## 📝 Label Maintenance

### Adding New Labels
1. **Discuss** with the team if a new label is needed
2. **Check** if an existing label could be used instead
3. **Create** the label with a clear description
4. **Document** the new label in this file
5. **Update** the ISSUE_TEMPLATES.md if needed

### Archiving Labels
- If a label is no longer needed, **archive it** (don't delete)
- Update this documentation to mark it as archived
- Example: If `work:le-horla` is complete, archive it but keep for historical reference

### Cleanup
- **Regularly review** labels for relevance
- **Merge similar** labels if they serve the same purpose
- **Remove unused** labels after confirming they're not needed

---

## 🏷️ Default Label Sets

### For a New Feature Issue:
- `priority:medium` (or high if critical)
- `type:feature`
- `category:*` (choose appropriate category)
- `work:*` (if work-specific)

### For a Bug Fix:
- `priority:high` (or medium if minor)
- `type:bug`
- `category:*` (choose appropriate category)

### For a Content Task:
- `priority:medium`
- `type:feature` or `type:chore`
- `category:content`
- `work:*` (work-specific label)

### For an Infrastructure Task:
- `priority:medium`
- `type:chore` or `type:feature`
- `category:infrastructure`

---

## 📌 Important Notes

1. **Consistency**: Always use the same label names and colors across the project
2. **Clarity**: Label descriptions should be clear and unambiguous
3. **Limit**: Don't create too many labels - aim for < 30 total
4. **Hierarchy**: Priority > Type > Category > Work-specific
5. **ADR-0011**: `needs-human` and `escalation` are special labels with specific workflows

---

## 🎯 Quick Reference Card

### Most Common Label Combinations:

| Issue Type | Priority | Type | Category | Example |
|------------|----------|------|----------|---------|
| New feature | `priority:medium` | `type:feature` | `category:frontend` | Add choice UI |
| Bug fix | `priority:high` | `type:bug` | `category:contract` | CI validation error |
| Content creation | `priority:medium` | `type:feature` | `category:content` | Complete Le Horla |
| Refactor | `priority:low` | `type:refactor` | `category:backend` | Improve onion layers |
| Documentation | `priority:low` | `type:documentation` | `category:documentation` | Update README |
| Infrastructure | `priority:high` | `type:chore` | `category:infrastructure` | Setup CI/CD |

---

*This configuration follows the project's constitutional documents and ADR-0011 (Agent Protocol).*
