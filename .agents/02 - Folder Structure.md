You are a senior systems architect establishing repository and file-structure standards.

Task:
Design the folder (directory) structure for PROJECT_NAME.

Context:
Project is an agent network platform for FAMILY_MEMORIES_APPLICATION. Stack: Cursor 2.0 agents, OpenCode modules, Python3 backend, Redis state-machine, microservices containerised, front-end separate (React/Next.js or equivalent), data lake for offline analysis. Testing, MLOps and monitoring are key. We need modularity, reuse, clear separation, developer onboarding simplicity, and alignment with CI/CD. 

Format:
1) Provide a top-level folder tree (use indentation to show structure)  
2) For each top-level folder include a short description of its purpose  
3) Specify naming conventions (folder names, file names) and versioning guidance  
4) Indicate where tests live, where documentation lives, and where Cursor/OpenCode artefacts live.

Constraints:
Avoid environment-specific folders (e.g., AWS only) at this stage — keep generic cloud-neutral. Use consistent naming style (e.g., snake_case or kebab-case). Highlight where Cursor2.0 agents and OpenCode modules appear.

Output:
Complete folder structure design with descriptive notes.