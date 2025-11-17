You are the INTEGRATION_ARCHITECT (or designated senior integration planner) for PROJECT_NAME.

Task:
Create a comprehensive Integration Plan for the module described in integration.mdc, ensuring full cohesion with the existing artifacts: folders.mdc, backend.mdc, frontend.mdc, AGENTS.md, and .cursorrules.

Context:
- PROJECT_NAME: SHORT_DESCRIPTION_OF_PROJECT  
- Domain: DOMAIN_DESCRIPTION (e.g. “family-memories agent network”)  
- Existing modules: BACKEND_MODULE (metadata in backend.mdc), FRONTEND_MODULE (metadata in frontend.mdc), AGENT_MODULES (described in AGENTS.md)  
- Repository structure: defined in folders.mdc  
- Behavioural rules: defined in .cursorrules  
- Integration module metadata: in integration.mdc (manual run-book style)  

Your plan should align with integration best-practices: clearly define why we integrate (goals), what systems/modules are involved, how data and state flows will be validated, and how the integration run will be governed. (See general sources on integration planning and system integration for reference.)  [oai_citation:0‡oneio.cloud](https://www.oneio.cloud/blog/system-integration-strategy?utm_source=chatgpt.com)

Requirements:
1. Create an **Objectives & Scope** section:  
   - Define integration goals (why), business value, impacted modules.  
   - Define scope (what is included, what is excluded).  
2. Create a **Systems & Modules Map** section:  
   - List each module being integrated (backend, frontend, agents) and map to folders in folders.mdc.  
   - For each module, list relevant metadata file (backend.mdc, frontend.mdc, integration.mdc) and current phase.  
   - Identify interfaces and APIs between modules.  
3. Create a **Data & State Flow Plan** section:  
   - Describe data models (referencing backend data model) and state-machine or agent-orchestration flows (as defined in agent architecture).  
   - Map data movement and state transitions across modules.  
   - Establish validation checkpoints and who/which agent is responsible.  
4. Create a **Integration Execution Plan** section:  
   - Define phases of integration (using phases from integration.mdc) and for each phase list: deliverables, responsibilities (which agent role from AGENTS.md), folder actions (which directories in folders.mdc), tests to run, manual vs automated tasks.  
   - Define environment (staging/integration environment) and execution trigger (manual invocation) in line with integration.mdc.  
5. Create a **Monitoring, Logging & Traceability Plan** section:  
   - Specify how observability (via LangSmith tracing, logs, metrics) will be captured.  
   - Define alert channels, logs directory paths (/integration/logs), issue registers (/integration/issues).  
   - Link to folders.mdc for where logs and issues live.  
6. Create a **Governance & Compliance Plan** section:  
   - Refer to .cursorrules: folder structure compliance, test coverage rules, documentation updates.  
   - Reference AGENTS.md: which agent role approves which step, how handoffs occur.  
   - Define sign-offs, versioning updates to metadata files (integration.mdc, backend.mdc, frontend.mdc).  
7. Create a **Risks, Dependencies & Open Questions** section:  
   - Identify integration risks (data mismatch, schema drift, API contract breakage, agent routing failures).  
   - Map dependencies (completion of backend phase X, frontend phase Y, agent role Z).  
   - List outstanding questions for back-end, front-end, agent or product teams.  

Constraints:  
- Do **not** write code.  
- Use placeholder names (e.g., MODULE_NAME, API_ENDPOINT, ENTITY_NAME) where appropriate.  
- Tie every module and folder reference back to folders.mdc.  
- Use language understandable to both technical and business stakeholders.  
- Make the plan actionable and ready for hand-off to integration/systems teams.

Output:  
A full **Integration Plan** document structured into the sections above. After the plan, list any follow-up questions needed to refine it further.