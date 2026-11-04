# Ira à toi - Project Plan (GitHub Milestones & Issues)

> **Status**: Ready for GitHub setup
> **Last Updated**: Initial version
> **Owner**: Alban Linard

---

## 📌 Overview

This document defines the **milestones** and **issues** for the "Ira à toi" project on **GitHub**.
These must be created manually in GitHub as the runtime does not have API access.

---

## 🎯 Milestones

### 1. **M0: Project Infrastructure & Validation**
- **Description**: Ensure the template, CI/CD, and contract validation are fully operational.
- **Due Date**: Sprint 1 (1-2 weeks)
- **Priority**: High
- **State**: Open

### 2. **M1: Complete Le Horla Pack**
- **Description**: Finalize Maupassant's Le Horla pack with all 60+ entries (currently only 5 entries as demo).
- **Due Date**: Sprint 2-3 (3-4 weeks)
- **Priority**: High
- **State**: Closed (will open after M0)

### 3. **M2: First Additional Work**
- **Description**: Add a second literary work to the collection (e.g., a correspondence or feuilleton).
- **Due Date**: Sprint 4 (2 weeks)
- **Priority**: Medium
- **State**: Closed

### 4. **M3: Frontend Integration**
- **Description**: Connect the React/TypeScript frontend to the contract system and implement the reading UI.
- **Due Date**: Sprint 5-6 (4 weeks)
- **Priority**: Medium
- **State**: Closed

### 5. **M4: Production Deployment**
- **Description**: Deploy to production CDN with all validated works.
- **Due Date**: Sprint 7 (1 week)
- **Priority**: High
- **State**: Closed

### 6. **M5: Monitoring & Maintenance**
- **Description**: Set up monitoring, analytics (non-intrusive), and maintenance processes.
- **Due Date**: Sprint 8 (2 weeks)
- **Priority**: Low
- **State**: Closed

---

## 📋 Issues by Milestone

---

### 🏗️ **M0: Project Infrastructure & Validation**

#### **Infrastructure**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M0-1 | Setup GitHub Actions CI/CD workflows | High | `infrastructure`, `ci-cd` | 4h | All workflows pass: `ci.yml`, `mutation.yml`, `release.yml`, `review.yml` |
| M0-2 | Configure pre-commit hooks | High | `infrastructure`, `quality` | 2h | `pre-commit run --all-files` passes on all files |
| M0-3 | Verify `make check` on all environments | High | `infrastructure`, `testing` | 4h | `make check` passes locally and in CI |
| M0-4 | Setup branch protection rules | High | `infrastructure`, `git` | 3h | `main` and `daily` branches protected, CI required |
| M0-5 | Verify release-please configuration | Medium | `infrastructure`, `release` | 2h | Changelog generation works, version bump follows Conventional Commits |

#### **Contract & Validation**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M0-6 | Run CI validation on Le Horla pack | High | `validation`, `contract` | 2h | `python ci/valider_pack.py oeuvres/le-horla-maupassant-1887` outputs "PRÊT POUR PUBLICATION" |
| M0-7 | Run full test suite | High | `validation`, `testing` | 2h | `python -m unittest discover -s tests -v` passes with 100% success |
| M0-8 | Verify mutation testing | Medium | `validation`, `testing` | 4h | `make mutate` runs without errors, no surviving mutants in critical code |
| M0-9 | Create additional negative tests for contract | Medium | `validation`, `testing` | 8h | Add tests for all edge cases in `contrat/pack.py` invariants |
| M0-10 | Document contract schema v1.1 | Medium | `documentation`, `contract` | 4h | Add comprehensive documentation for all contract fields and rules |

#### **Agent Protocol**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M0-11 | Setup reviewer agent workflow | High | `agents`, `infrastructure` | 4h | Reviewer agent runs on PRs, exit code determines merge status |
| M0-12 | Test day cycle automation | High | `agents`, `process` | 4h | `make day-start`, `make day-report`, `make smoke-test` work end-to-end |

---

### 📖 **M1: Complete Le Horla Pack**

#### **Text Preparation**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M1-1 | Source complete Le Horla text from Wikisource | High | `content`, `le-horla` | 8h | Full text (all entries) verified against Wikisource, domain public proof documented |
| M1-2 | Create complete fragments.json for all entries | High | `content`, `le-horla` | 16h | All ~60 entries split into fragments, each with proper `ancrage_fictif` |

#### **Micro-interactions**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M1-3 | Design corruption mechanics for each entry | High | `content`, `design`, `le-horla` | 24h | Each corruption documented with condition (typically `relu`) and word replacements |
| M1-4 | Design choice mechanics | Medium | `content`, `design`, `le-horla` | 16h | At least 5 meaningful choices throughout the journal |
| M1-5 | Design writing prompts | Medium | `content`, `design`, `le-horla` | 12h | At least 3 writing gestures with proper `max_caracteres` |
| M1-6 | Design find mechanics | Medium | `content`, `design`, `le-horla` | 8h | At least 3 "trouver" gestures with corruption targets |
| M1-7 | Design mirror mechanics | Medium | `content`, `design`, `le-horla` | 8h | At least 3 mirror states that render player's writing |

#### **Cadences**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M1-8 | Create standard cadence | High | `content`, `cadence`, `le-horla` | 8h | Realistic timing (3-4 weeks for full journal), respecting narrative flow |
| M1-9 | Create sprint cadence for QA | Medium | `content`, `cadence`, `le-horla` | 4h | Compressed timing for testing (1-2 weeks) |
| M1-10 | Create optional "immersion" cadence | Low | `content`, `cadence`, `le-horla` | 4h | Slower pace for deep reading experience |

#### **Enrichissements**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M1-11 | Create character fiches | Medium | `content`, `enrichissements`, `le-horla` | 12h | Fiches for main characters with domain public proof |
| M1-12 | Create lexique | Medium | `content`, `enrichissements`, `le-horla` | 8h | Lexique for historical/technical terms, IA-generated then validated |
| M1-13 | Create historical notes | Low | `content`, `enrichissements`, `le-horla` | 8h | Notes on historical context, properly sourced |

#### **Assets**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M1-14 | Source domain-public cover image | Medium | `assets`, `le-horla` | 4h | Cover image with creator (death +70 years), source, license, hash |
| M1-15 | Source typography assets | Medium | `assets`, `le-horla` | 4h | Display fonts (OFL license) for dates, titles, seals |

#### **Validation**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M1-16 | Run CI validation on complete pack | High | `validation`, `le-horla` | 2h | All 7 CI checks pass, "PRÊT POUR PUBLICATION" |
| M1-17 | Add negative tests for new mechanics | High | `validation`, `testing`, `le-horla` | 8h | Tests for all new invariants in the complete pack |

---

### 🎨 **M2: First Additional Work**

#### **Selection & Research**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M2-1 | Select second work for collection | High | `content`, `research` | 4h | Work selected: domain public verified, fits collection theme (Cabinet Noir) |
| M2-2 | Source complete text | High | `content`, `research` | 8h | Full text sourced from Gallica/Wikisource, domain public proof |

#### **Implementation**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M2-3 | Create manifeste.json | High | `content`, `manifest` | 2h | Proper metadata, author, source, licenses |
| M2-4 | Create fragments.json | High | `content`, `fragments` | 16h | Complete text splitting with proper anchors |
| M2-5 | Design micro-interactions | High | `content`, `design` | 16h | Corruptions, choices, writings, find mechanics |
| M2-6 | Create cadences | Medium | `content`, `cadence` | 8h | At least 2 cadences (standard + sprint) |
| M2-7 | Create enrichissements | Medium | `content`, `enrichissements` | 8h | Fiches, lexique, notes with proper attribution |
| M2-8 | Run CI validation | High | `validation` | 2h | Pack passes all CI checks |

---

### 🖥️ **M3: Frontend Integration**

#### **Core UI**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M3-1 | Setup Vite + React + TypeScript | High | `frontend`, `infrastructure` | 4h | `make web-install` works, dev server starts |
| M3-2 | Implement reading view | High | `frontend`, `ui` | 24h | Displays fragment text with proper typography and styling |
| M3-3 | Implement corruption rendering | High | `frontend`, `ui`, `contract` | 16h | Corrupted words displayed based on active states, original text preserved |
| M3-4 | Implement mirror rendering | High | `frontend`, `ui`, `contract` | 12h | Player's writing displayed as annotations, never in main text |

#### **Interactions**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M3-5 | Implement choice UI | High | `frontend`, `ui`, `interactions` | 16h | Choices displayed, selection triggers state changes |
| M3-6 | Implement writing UI | High | `frontend`, `ui`, `interactions` | 20h | Text input with character limit, saved to player state |
| M3-7 | Implement find UI | Medium | `frontend`, `ui`, `interactions` | 12h | Word selection mechanism for "trouver" gestures |
| M3-8 | Implement state management | High | `frontend`, `state` | 24h | Player states persisted, conditions evaluated correctly |

#### **Cadences & Scheduling**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M3-9 | Implement personal clock | High | `frontend`, `scheduling` | 24h | `due_at` calculated based on last read, rules, constraints |
| M3-10 | Implement notification system | Medium | `frontend`, `notifications` | 16h | Push notifications for new fragments (opt-in) |
| M3-11 | Handle night opt-in | Medium | `frontend`, `ux` | 8h | Explicit opt-in for night pushes, with preview |

#### **Polish**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M3-12 | Implement typography skins | Medium | `frontend`, `ui`, `peau` | 12h | Display fonts applied based on `peau` configuration |
| M3-13 | Add color theme support | Medium | `frontend`, `ui`, `peau` | 8h | Color palette from `peau` applied to UI |
| M3-14 | Implement responsive design | Medium | `frontend`, `ui` | 12h | Works on mobile, tablet, desktop |
| M3-15 | Add accessibility features | Medium | `frontend`, `a11y` | 12h | WCAG 2.1 AA compliance, keyboard navigation |

#### **Testing**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M3-16 | Frontend unit tests | High | `frontend`, `testing` | 16h | 90%+ coverage on all frontend code |
| M3-17 | Frontend integration tests | Medium | `frontend`, `testing` | 8h | Key user flows tested |

---

### 🚀 **M4: Production Deployment**

#### **Infrastructure**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M4-1 | Setup production CDN | High | `infrastructure`, `cdn` | 8h | CDN configured, packs can be published |
| M4-2 | Setup monitoring | High | `infrastructure`, `monitoring` | 8h | Health checks, error tracking, performance metrics |
| M4-3 | Setup logging | Medium | `infrastructure`, `logging` | 4h | Structured logs in production, no secrets |

#### **Deployment**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M4-4 | Deploy notify service | High | `infrastructure`, `notify` | 4h | Notification pipeline working in production |
| M4-5 | Deploy frontend | High | `frontend`, `deployment` | 4h | Frontend accessible, all features working |
| M4-6 | Deploy first works | High | `content`, `deployment` | 4h | Le Horla and second work published to CDN |
| M4-7 | Verify production CI | High | `infrastructure`, `ci-cd` | 4h | All CI workflows pass in production environment |

#### **Security**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M4-8 | Security audit | High | `security` | 8h | No vulnerabilities in dependencies, secrets not exposed |
| M4-9 | Setup backup strategy | Medium | `infrastructure`, `backup` | 4h | Regular backups, recovery procedure documented |

---

### 📊 **M5: Monitoring & Maintenance**

#### **Monitoring**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M5-1 | Setup usage analytics | Medium | `monitoring`, `analytics` | 8h | Non-intrusive analytics (no player data, no carnet analysis) |
| M5-2 | Setup error tracking | Medium | `monitoring` | 4h | Errors logged and alerted |
| M5-3 | Create dashboard | Low | `monitoring` | 4h | Overview of active readers, pack downloads |

#### **Maintenance**
| # | Title | Priority | Labels | Estimate | Acceptance Criteria |
|---|-------|----------|--------|----------|---------------------|
| M5-4 | Document maintenance procedures | Medium | `documentation`, `maintenance` | 4h | Runbook for common issues, escalation paths |
| M5-5 | Setup automated updates | Low | `maintenance` | 4h | Dependencies updated regularly, security patches applied |

---

## 🏷️ Labels Configuration for GitHub

GitHub labels should be created in **Settings → Issues → Labels → New label**

### Priority Labels
| Name | Color | Description |
|------|-------|-------------|
| `priority: high` | `#D73A4A` (Red) | Critical, blocks other work |
| `priority: medium` | `#FBCA04` (Yellow) | Important, should be done soon |
| `priority: low` | `#0E8A16` (Green) | Nice to have, backlog |

### Category Labels
| Name | Color | Description |
|------|-------|-------------|
| `category: infrastructure` | `#6F42C1` (Purple) | CI/CD, Docker, tooling |
| `category: content` | `#1D76DB` (Blue) | Literary works, fragments, enrichissements |
| `category: frontend` | `#006B75` (Teal) | React, TypeScript, UI/UX |
| `category: backend` | `#000000` (Black) | Python, services, models |
| `category: testing` | `#E66600` (Orange) | Tests, validation, CI tests |
| `category: documentation` | `#5319E7` (Violet) | Docs, ADRs, guides |
| `category: validation` | `#11E109` (Light Green) | Contract validation, CI checks |
| `category: design` | `#FF77CC` (Pink) | Interaction design, UX |
| `category: research` | `#7C3AED` (Dark Violet) | Source finding, domain public verification |
| `category: security` | `#D93F0B` (Dark Red) | Security, secrets, audits |
| `category: agents` | `#F98400` (Dark Orange) | Agent protocol, reviewer, notifications |
| `category: maintenance` | `#576474` (Gray) | Updates, backups, monitoring |

### Type Labels
| Name | Color | Description |
|------|-------|-------------|
| `type: feature` | `#1D76DB` (Blue) | New feature development |
| `type: bug` | `#D73A4A` (Red) | Bug fix |
| `type: chore` | `#576474` (Gray) | Maintenance chore |
| `type: refactor` | `#6F42C1` (Purple) | Code refactoring |
| `type: documentation` | `#5319E7` (Violet) | Documentation work |

### Work-Specific Labels
| Name | Color | Description |
|------|-------|-------------|
| `work: le-horla` | `#1D76DB` (Blue) | Le Horla by Maupassant |
| `work: second-oeuvre` | `#0E8A16` (Green) | Second literary work |
| `contract` | `#E66600` (Orange) | Contract schema |
| `cadence` | `#6F42C1` (Purple) | Cadence/pacing |
| `ui` | `#006B75` (Teal) | User interface |
| `interactions` | `#F98400` (Dark Orange) | Micro-interactions |
| `assets` | `#11E109` (Light Green) | Assets |

### Process Labels
| Name | Color | Description |
|------|-------|-------------|
| `needs-human` | `#D73A4A` (Red) | Requires human decision (per ADR-0011) |
| `blocked` | `#D93F0B` (Dark Red) | Blocked by another issue |
| `escalation` | `#E66600` (Orange) | Escalated to human |
| `review` | `#FBCA04` (Yellow) | Needs code/design review |
| `wip` | `#576474` (Gray) | Work in progress |
| `ready` | `#0E8A16` (Green) | Ready for work |

---

## 📅 Suggested Timeline

### Sprint 1 (Week 1-2): M0 - Infrastructure
- Focus: Get all validation and CI/CD working
- Deliverable: Template is ready for content creation

### Sprint 2 (Week 3): M0 Completion + M1 Start
- Complete remaining M0 tasks
- Start Le Horla text sourcing

### Sprint 3-4 (Week 4-7): M1 - Complete Le Horla
- Focus: All entries, interactions, validation
- Deliverable: Complete, validated Le Horla pack

### Sprint 5 (Week 8): M2 Start + M3 Start
- Begin second work
- Start frontend implementation

### Sprint 6-7 (Week 9-12): M3 - Frontend
- Focus: Complete frontend integration
- Deliverable: Working PWA with all features

### Sprint 8 (Week 13): M2 Completion + M4
- Complete second work
- Deploy to production

### Sprint 9 (Week 14): M4 Completion + M5
- Final deployment tasks
- Setup monitoring

---

## 🎯 Success Metrics

### M0 (Infrastructure)
- [ ] All CI workflows pass
- [ ] `make check` passes on all environments
- [ ] Template is ready for new works

### M1 (Le Horla)
- [ ] Complete pack with all ~60 entries
- [ ] All micro-interactions designed and validated
- [ ] CI validation passes
- [ ] Negative tests cover all edge cases

### M2 (Second Work)
- [ ] Second work selected and sourced
- [ ] Complete pack with interactions
- [ ] CI validation passes

### M3 (Frontend)
- [ ] All UI components implemented
- [ ] All interactions working
- [ ] 90%+ frontend test coverage
- [ ] Responsive design verified

### M4 (Production)
- [ ] All works deployed to CDN
- [ ] Monitoring and logging in place
- [ ] Security audit passed

### M5 (Maintenance)
- [ ] Monitoring dashboard operational
- [ ] Maintenance procedures documented

---

## 📝 Notes

1. **Work Selection**: The second work (M2) should be chosen from the public domain and fit the "Cabinet Noir" collection theme.

2. **IA Assistance**: IA can be used to:
   - Generate initial fragment splits (MUST be validated by human)
   - Generate enrichissements (MUST be validated and attributed)
   - Suggest interaction mechanics (MUST be approved by human)
   - **NEVER** rewrite source text or analyze player content

3. **Quality Gates**: Every merge to `daily` requires:
   - CI green
   - Reviewer status check green (0 BLOCKING findings)
   - Not on escalation list

4. **Conventional Commits**: All commits must follow the Conventional Commits format.

5. **ADRs**: Any non-trivial architectural decision should be documented as an ADR in `docs/decisions/`.

---

## ✅ Next Steps

1. **Create GitHub repository** (if not already created)
2. **Push local repository** to GitHub
3. **Create labels** in GitHub (Settings → Issues → Labels)
4. **Create milestones** in GitHub (Issues → Milestones)
5. **Create issues** for M0 using the templates below
6. **Assign issues** to team members or sprints
7. **Begin work** on M0-1: Setup GitHub Actions CI/CD workflows

---

*This plan follows the project's constitutional documents (AGENTS.md, ASSISTANCE_IA.md, docs/architecture.md, docs/branching.md).*
