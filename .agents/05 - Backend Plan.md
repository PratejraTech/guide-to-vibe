You are a senior backend architect and data-model–first systems designer.

Goal:
Design a detailed BACKEND_PLAN for PROJECT_NAME, starting explicitly from the DATA MODEL and then expanding into services, APIs, storage, and observability.

Context:
- PROJECT_NAME: SHORT_DESCRIPTION_OF_PROJECT
- Domain: DOMAIN_DESCRIPTION (e.g. “agentic development observability”, “family memories app”, etc.)
- Backend stack: BACKEND_STACK (e.g. Python 3 + FastAPI, Postgres, Redis, LangGraph/LangChain, etc.)
- Infra: INFRASTRUCTURE_CONTEXT (e.g. Docker/K8s, Cloudflare Workers backend, AWS/GCP, etc.)
- We use Cursor 2.0 and OpenCode for development and agentic workflows.
- There is (or will be) a shared FOLDER STRUCTURE defined in folders.mdc in the repo root.

Primary requirement:
The backend plan MUST start from a clear, well-structured DATA MODEL, then derive services, APIs, and persistence from it.

Tasks:
1. Propose a canonical DATA MODEL:
   - List key entities (TABLES / COLLECTIONS / Pydantic MODELS) and their fields.
   - Identify relationships (one-to-many, many-to-many, etc.).
   - Map entities to FOLDER STRUCTURE MODULES (e.g. /backend/DOMAIN/models, /backend/DOMAIN/db, etc.).
   - Include any derived/analytical views if relevant.

2. From the DATA MODEL, derive the BACKEND ARCHITECTURE PLAN:
   - Application layers (e.g. schemas/models, repositories, services, routers/controllers).
   - For each layer, reference the corresponding folder(s) from folders.mdc.
   - Define key API endpoints (only as descriptions, not code) and how they map to entities.
   - Define validation and data-quality responsibilities (where validation lives in the stack).

3. Operational Concerns:
   - Outline how logging, tracing, metrics and MLOps hooks are integrated into backend components.
   - Identify how the backend will expose signals usable by agentic tools (Cursor 2.0, OpenCode, LangSmith).
   - Describe error-handling strategy and how errors/alerts flow through the system.

4. Phased Delivery Plan:
   - Break the backend into PHASES (e.g. Phase 1: Core Data Model + CRUD; Phase 2: Business Logic; Phase 3: Integrations; Phase 4: Performance & Observability).
   - For each phase, list objectives, deliverables, and dependencies.
   - Always reference which folders will be created/modified (aligned with folders.mdc).

Format:
- Section 1: Data Model Overview
- Section 2: Backend Architecture derived from Data Model
- Section 3: Operational & MLOps Concerns
- Section 4: Phase-by-Phase Implementation Plan
- Section 5: Open Questions / Assumptions

Constraints:
- Do NOT write code.
- Use generic placeholders for entity and field names where necessary (e.g. ENTITY_NAME, FIELD_NAME).
- Always tie back to the existing or planned folder structure defined in folders.mdc.
- Make the plan concrete enough that a senior backend engineer could immediately start breaking it into tasks.

Output:
Produce the BACKEND_PLAN in clear sections as specified above, then list any clarifying questions you need to refine the data model.