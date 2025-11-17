# Guide to Vibe

Welcome to the **Guide to Vibe** — the canonical specification and protocol suite for agent-driven, modular, and well-governed software development. This documentation serves as both onboarding material and operational standard for all contributors, human or agent, working within the repository.

---

## Overview

Guide to Vibe defines:  
- **Agent roles and responsibilities**  
- **Repository structure and folder governance**  
- **Development and documentation protocols**  
- **Testing, integration, and refactor rules**  
All processes are enforced by machine-readable metadata, human-readable docs, and phase-based development logic.

**Key governing documents:**
- [`AGENTS.md`](./AGENTS.md) — Standard agent roles and workflows
- `.cursorrules` — Policy and enforcement for agent/module behaviour
- `folders.mdc` — Repository folder structure (source of truth)
- Module specs: `backend.mdc`, `frontend.mdc`, `integration.mdc`, `refactor.mdc`, `testing.mdc`, etc.
- Playbooks and architecture docs under `/docs/`

---

## Quick Start

1. **Read `AGENTS.md`** for agent roles and handoff logic.
2. **Always consult `.cursorrules`** before editing, committing, or adding folders.
3. **Adhere strictly to `folders.mdc`**; never create rogue or undocumented folders.
4. **Follow the phase protocol:**
    - Complete implementation
    - Write & pass tests
    - Update documentation and metadata
5. **Log all issues** in the appropriate `/issues/` directory (by module).
6. For new agent types or extensions, update all relevant MDC and metadata files per the governance protocol.

---

## Agent Roles (Summary)

- **ARCHITECT_AGENT**: Governs structure, approves/denies module and folder changes.
- **BACKEND_AGENT**: Implements backend logic, services, and tests in `/backend/`.
- **FRONTEND_AGENT**: Implements UI, components, and frontend logic in `/frontend/`.
- **INTEGRATION_AGENT**: Coordinates integration tests and cross-agent flows.
- **QA_AGENT**: Ensures contract/test coverage and reports quality gaps.
- **DOCS_AGENT**: Writes/updates documentation MDX in `/docs/` after sweeps or major changes.
- **ANALYST_AGENT**: Aligns product/requirements with technical design and agent flows.
- _Domain/extension agents_ (add as needed — see `AGENTS.md` and section 7 in same).

See full details in [`AGENTS.md`](./AGENTS.md).

---

## Development Protocols

- **Documentation** must reflect actual code and folder state. See [`documentation.mdc`](./cursor/rules/documentation.mdc).
- **Testing** is mandatory for all modules before merging (see [`testing.mdc`](./cursor/rules/testing.mdc)).
- **Refactoring** requires documentation, planning, and conformity checks (see [`refactor.mdc`](./cursor/rules/refactor.mdc)).
- **Integration** is orchestrated via playbooks, using metadata to define and validate flows (see [`integration.mdc`](./cursor/rules/integration.mdc)).

---

## Folder Structure

All folders and files must match the canonical definition in `folders.mdc`.  
- **No new modules/folders/types** without architect approval.
- All agent and test files must be placed as dictated by this structure.

---

## Documentation Sweep

- Periodically, DOCS_AGENT runs a sweep to extract production-ready docs for each module, feature, and API.
- Generates `.mdx` files under `/docs/`, strictly directory-aligned.
- Must be run before releases and after major refactors.

See [`documentation.mdc`](./cursor/rules/documentation.mdc) for the required sweep process.

---

## Compliance & Change Process

- **Versioning**: All metadata/docs are versioned; update `version` and `last_updated` when changing agent roles, structure, or protocols.
- **Changelog**: All significant changes are recorded under `/docs/changelog/`.
- **Conflict Resolution** and schema/contract mismatches escalate per agent role (see `AGENTS.md`).

---

## Best Practices

- **Read** `.cursorrules` and `folders.mdc` before making changes.
- **Synchronize** docs and code before merges.
- **Review** agent protocols for clarity and onboarding ease.
- **Update** module metadata at every phase and after handoff.

---

## Contributing

1. Fork or branch as usual, but adhere strictly to this documentation.
2. All PRs must include tests, updated docs, and metadata bumps.
3. Open a discussion in `/integration/issues/` for any structural or contract concerns.

---

## References

- [Agent Operating Specification](./AGENTS.md)
- [Documentation Protocol](./cursor/rules/documentation.mdc)
- [Testing Protocol](./cursor/rules/testing.mdc)
- [Refactoring Rules](./cursor/rules/refactor.mdc)
- [Integration Protocol](./cursor/rules/integration.mdc)
- [`folders.mdc`](./.agents/folders.mdc) — Source of truth for the repo layout

---

For more, see agent role and metadata files, or reach out to the repository maintainers.

Let the vibe guide your contribution!

