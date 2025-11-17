# AGENTS — Operating Specification  
Project: PROJECT_NAME  
Version: 1.0  
Last Updated: YYYY-MM-DD  
Status: Active  

## 1. Purpose & Scope  
This document defines the canonical set of agents, their roles, inputs, outputs, interaction rules, and governance within the PROJECT_NAME repository.  
It is aligned with:  
- `folders.mdc` (source of truth for repository structure)  
- `.cursorrules` (governance for agent behaviour and structure)  
- `backend.mdc`, `frontend.mdc`, `integration.mdc` (module-metadata)  
- The “Guide to Vibe” protocol for advanced development with Cursor 2.0 and OpenCode  

The aim: to provide clear, consistent, maintainable agent documentation that supports team alignment, onboarding, and scalability.  
(This aligns with software-documentation best practices: clear audience, consistent structure, versioning, review cycle.)  [oai_citation:0‡atlassian.com](https://www.atlassian.com/blog/loom/software-documentation-best-practices?utm_source=chatgpt.com)

---

## 2. Agent Roles  
Below are the standard agent roles for PROJECT_NAME. Each role is defined with responsibilities, inputs, outputs, and folder/structure alignment. Additional domain-specific agents may be added later—see Section 8.

### 2.1 ARCHITECT_AGENT  
**Role Purpose:**  
Define system-wide architecture, validate structural coherence, enforce adherence to repository structure.  
**Responsibilities:**  
- Review and approve changes to `folders.mdc`, architecture plans, module‐metadata files (`backend.mdc`, `frontend.mdc`, etc.).  
- Ensure data-model, API contract and agent workflows align across modules.  
- Gate structural modifications (new folders/modules) unless documented and approved.  
**Inputs:**  
`folders.mdc`, architecture documents, module-metadata files.  
**Outputs:**  
Architecture review logs (under `/docs/architecture/`), updated module metadata, change requests.  
**Folder Alignment:**  
Reads/writes under `/docs/architecture/`, triggers updates in module folders defined in `folders.mdc`.

---

### 2.2 BACKEND_AGENT  
**Role Purpose:**  
Implement backend functionality in accordance with data models, API contracts, folder structure, and module metadata.  
**Responsibilities:**  
- Convert data-model definitions into backend models, services, controllers, following `backend.mdc` phases.  
- Ensure module development adheres to `folders.mdc` (“no rogue folders”).  
- Create test harnesses under `/backend/tests/` (as defined in folder structure).  
- Update `backend.mdc` with phase completion metadata.  
**Inputs:**  
`backend.mdc`, `folders.mdc`, `.cursorrules`.  
**Outputs:**  
Backend modules, test files, updated metadata, issue logs.

---

### 2.3 FRONTEND_AGENT  
**Role Purpose:**  
Develop frontend screens/components and integrations aligned with backend API contracts, data-models, and frontend module metadata.  
**Responsibilities:**  
- Derive TypeScript/flow/view‐models from backend data model (conceptually) and implement UI artifacts.  
- Place components, views, features strictly according to folder layout defined in `folders.mdc`.  
- Write component + integration tests in `/frontend/tests/`.  
- Update `frontend.mdc` on phase completion.  
**Inputs:**  
`frontend.mdc`, `folders.mdc`, `.cursorrules`, backend API descriptions.  
**Outputs:**  
Frontend modules, tests, metadata updates.

---

### 2.4 INTEGRATION_AGENT  
**Role Purpose:**  
Coordinate and execute end-to-end flows, integration tests (manual or automated) across backend, frontend, and agent network.  
**Responsibilities:**  
- Execute the integration runbook defined in `integration.mdc`.  
- Validate API contracts, agent orchestration, state-machine transitions, tracing/observability.  
- Log results to `/integration/logs/`, record issues in `/integration/issues/`.  
- Update `integration.mdc` metadata (open_issues, assumptions).  
**Inputs:**  
`integration.mdc`, `backend.mdc`, `frontend.mdc`, system logs/traces.  
**Outputs:**  
Integration logs, issue register, updated metadata.

---

### 2.5 QA_AGENT  
**Role Purpose:**  
Ensure quality, correctness, schema/contract conformance, test coverage across modules and agent flows.  
**Responsibilities:**  
- Validate schemas, data contracts, UI flows, agent interactions.  
- Check that each development phase has corresponding tests and documentation.  
- Report test failures, coverage gaps, contract violations.  
**Inputs:**  
All module metadata files, test suites, logs.  
**Outputs:**  
QA reports, test-improvement tasks.

---

### 2.6 DOCS_AGENT  
**Role Purpose:**  
Maintain the documentation ecosystem: ensure that MDC files, architecture docs, runbooks remain accurate, versioned, and accessible.  
**Responsibilities:**  
- Update documentation whenever architecture, contracts or flows change.  
- Ensure versioning (e.g., metadata fields `version`, `last_updated`) are maintained.  
- Enforce documentation review cycle.  
**Inputs:**  
Module metadata files, architecture docs, commit history.  
**Outputs:**  
Docs updates under `/docs/`, changelog entries.

---

### 2.7 ANALYST_AGENT  
**Role Purpose:**  
Bridge product and technical teams by refining requirements, identifying gaps, and translating business goals into module metadata and agent tasks.  
**Responsibilities:**  
- Collaborate on PRD, ensure module metadata aligns with product objectives.  
- Identify missing requirements or misalignments between product, backend, frontend, agent workflows.  
**Inputs:**  
PRD document, module metadata (backend.mdc, etc.), architectural strategy.  
**Outputs:**  
Revised requirements, updated metadata, gap-analysis reports.

---

## 3. Agent Interaction & Workflow  
### Shared Ground Rules  
- All agents must conform to `folders.mdc` (the definitive structure).  
- All agents must abide by `.cursorrules` (behavioural & structural rules).  
- Agents should not create new folders or module types without approval from ARCHITECT_AGENT.  
- Agents must update module metadata (e.g., backend.mdc) after each phase.  
- Tests must accompany each feature/phase before progressing.  
- Discrepancies must be logged into the appropriate `/issues/` directory.  

### Handoff Protocol  
- Handoff occurs when an agent updates its metadata file and marks phase completion.  
- The next agent reads the updated metadata before proceeding.  
- Example: BACKEND_AGENT completes phase → updates `backend.mdc` → signals FRONTEND_AGENT to proceed.

### Conflict Resolution  
- Structural conflicts (folders/architecture) → escalate to ARCHITECT_AGENT.  
- Requirements ambiguities → escalate to ANALYST_AGENT.  
- Contract mismatches (API/data) → escalate to INTEGRATION_AGENT.  
- Quality / test failures → QA_AGENT handles and flags to relevant agents.

---

## 4. Phase-Based Development Logic  
Agents must operate in discrete phases as defined in module metadata (backend.mdc, frontend.mdc, integration.mdc).  
**Phase completion criteria**:  
- Implementation done  
- Tests written & passing  
- Documentation (metadata + docs) updated  
- Integration/contract validation (if required)  

Next phase cannot start until all criteria are met—or a formal exception is approved by ARCHITECT_AGENT.

---

## 5. Documentation & Governance Standards  
- Version and date must appear on each agent metadata and MDC file.  
- Documentation as code: all documents maintained in version control, templated, reviewed regularly.  [oai_citation:1‡Full Scale](https://fullscale.io/blog/software-documentation-best-practices-outsourced-development/?utm_source=chatgpt.com)  
- Use templates for consistency.  [oai_citation:2‡Daily.dev](https://daily.dev/blog/10-internal-documentation-best-practices-for-dev-teams?utm_source=chatgpt.com)  
- Keep documentation lightweight, searchable, and focused on value (what the team needs).  [oai_citation:3‡Scribe](https://scribe.com/library/best-practices-software-documentation?utm_source=chatgpt.com)  
- Review documentation periodically, include feedback loops.  [oai_citation:4‡atlassian.com](https://www.atlassian.com/blog/loom/software-documentation-best-practices?utm_source=chatgpt.com)  

---

## 6. Accessibility & Maintainability  
- All agent roles and documentation must use consistent terminology and structure.  
- Metadata fields must be machine-readable (for pipeline/agent introspection) and human-readable (for team).  
- Must support easy onboarding of new team members (agents or humans).  
- Cross-references (links between MDC files, runbooks, docs) must be maintained.  

---

## 7. Extension and Custom Agent Roles  
The architecture supports extension. Additional agents may be defined as needed, e.g.:  
- DOMAIN_AGENT (business/domain logic)  
- DATA_AGENT (ETL, MLOps pipelines)  
- UI/UX_AGENT (frontend-specialised)  
- SECURITY_AGENT (policy, role-based controls)  
- PERFORMANCE_AGENT (scalability, stress testing)  

Each new role must be documented here (role purpose, responsibilities, inputs, outputs) and referenced in `folders.mdc` as required.

---

## 8. Revision & Versioning Process  
Whenever agents/structure change, you must:  
1. Update `AGENTS.md` version and `last_updated` date.  
2. Document change in `/docs/changelog/`.  
3. Ensure `.cursorrules`, `folders.mdc`, module metadata (backend.mdc, etc.) reflect the change.  
4. Re-run any relevant manual verification via INTEGRATION_AGENT (see `integration.mdc`).  

---

## 9. Compliance with Cursor & Agent-Work Rules  
- Agents must read `.cursorrules` before executing tasks.  
- No deviations from `folders.mdc` without formal request and approval.  
- Metadata updates must happen as soon as phases complete.  
- Agents must log all operations in relevant `/logs/` directories for traceability.  