# Google Technical Discovery — Required Written Answers

Prepared from the November 18, 2026 AI architecture discussion. Speaker comments are leads for verification, not product commitments.

## 1. Agent identity and governance

- Which Google Cloud services establish workload identity for agents, tools, and delegated tasks?
- How is agent identity tied to a human sponsor, business purpose, and legal entity record?
- What audit evidence is available for identity resolution, delegation, approvals, and tool calls?
- Which controls are enforced at the gateway versus merely described in agent instructions?

## 2. Independent emergency stop

- Can a control-plane operator block all new agent tool calls independently of the agent runtime?
- Can queued and in-flight work be paused or cancelled?
- How are delegated credentials and provider sessions revoked?
- What are the documented propagation delays and failure modes?
- Can the control work if the orchestration layer or model provider is unavailable?

## 3. Security coverage

- What does Model Armor inspect and enforce across prompts, retrieved content, tool inputs/outputs, attachments, and egress?
- Which third-party model and tool paths are covered?
- How are prompt injection, data exfiltration, sensitive data, and untrusted MCP servers handled?
- Which logs prove that a policy was enforced?

## 4. Cost enforcement

- Which budget controls are alerts only, and which actually block requests?
- Are hard limits available by project, agent, user, model, and tool?
- What happens to long-running sessions and in-flight requests at a limit?
- What overage or delayed-metering conditions exist?
- Can costs be exported with stable agent and project identifiers?

## 5. Portability and model routing

- Which agent definitions, skills, tools, evaluation cases, and policies are portable?
- Can a non-Google model be substituted without rewriting business logic?
- What is the supported interface for external model providers?
- How are model versions pinned, evaluated, and rolled back?

## 6. Production lifecycle

- What are the current GA, preview, and roadmap statuses for each component shown?
- Which services are separately licensed or billed?
- What reference architecture and threat model are supported?
- Which implementation milestones must be met before a bounded workflow enters production?

Request written documentation, feature availability, licensing details, architecture diagrams, and a named technical owner for each answer.
