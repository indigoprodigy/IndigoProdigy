# Universoul Agent Governance Standard

**Version:** 1.0  
**Status:** Public reference standard  
**Applies to:** Agent prototypes and future approved integrations

## 1. Purpose

Establish a consistent control framework for agent identity, authority, tool access, human oversight, evidence, and operational accountability. This document describes a target standard, not a claim that all controls are currently implemented.

## 2. Non-negotiable principles

- The legal entity and authorized human principals retain decision authority.
- Agents receive delegated, scoped permissions; they do not own assets or independently create legal authority.
- Default-deny access is required for tools and resources.
- Every consequential action must have an explicit approval policy.
- Agent identity, human sponsor, project, policy version, and execution context must be attributable.
- Every action must be auditable without logging secrets or unnecessary personal data.
- Emergency stop must be independent of the agent being stopped.
- Provider portability must be designed into model and tool interfaces.

## 3. Agent registration record

Each agent should have a registry entry containing:

| Field | Requirement |
|---|---|
| Agent ID | Stable, unique identifier |
| Display name | Human-readable name |
| Owner / sponsor | Authorized human and responsible legal entity |
| Purpose | Approved business purpose |
| Environment | Development, test, or production |
| Model provider | Provider and model identifier |
| Tool allowlist | Explicit approved tools |
| Data classification | Highest data class the agent may access |
| Approval policy | Actions requiring human approval |
| Budget | Approved limit and alert thresholds |
| Stop control | Independent stop mechanism and owner |
| Policy version | Version/hash of effective policy |
| Review date | Next access and risk review |

Do not place credentials, private keys, or personal identity documents in the registry.

## 4. Permission tiers

1. **Observe:** read approved public or synthetic information.
2. **Draft:** prepare content or proposed changes without sending or publishing.
3. **Execute reversible:** perform approved, reversible actions within a narrow scope.
4. **Consequential:** external communications, purchases, financial movement, permission changes, public release, legal/tax submissions, or production changes. Require explicit human approval.
5. **Prohibited:** actions outside the approved purpose, unlawful activity, credential disclosure, unauthorized access, or destructive actions without an approved change process.

## 5. Identity and accountability

Technical service identity is not the same as legal identity. Use provider IAM or workload identity for technical authentication, and maintain a separate governance record tying each agent to its sponsor, authorized purpose, and approval chain. Legal ownership and authority must be confirmed by counsel and governing documents; software metadata alone cannot establish them.

## 6. Execution lifecycle

1. Register the agent and sponsor.
2. Approve purpose, data scope, tools, model, and budget.
3. Test against synthetic data.
4. Evaluate policy enforcement, prompt-injection resistance, and failure handling.
5. Enable limited pilot access with human review.
6. Measure quality, safety, cost, latency, and business value.
7. Expand only after a documented stage-gate review.
8. Revoke or suspend access when purpose, risk, or authorization changes.

## 7. Required evidence

Maintain records of policy approvals, agent versions, tool calls, decision outcomes, human approvals, errors, stop events, cost attribution, and periodic access reviews. Logs should be access-controlled, tamper-evident, time-synchronized, and privacy-minimized.

## 8. Provider portability

Keep agent instructions, tool schemas, policy definitions, evaluation cases, and business data in portable formats where practical. Place model selection behind a provider adapter or gateway. Avoid embedding provider-specific assumptions in business logic. Document model-specific behavior and fallback rules.

## 9. Exceptions

Exceptions must identify the approving human, reason, scope, duration, compensating controls, and expiration date. No permanent exception by silence.

## 10. Relationship to law and contracts

This standard is operational guidance, not legal advice. Entity ownership, fiduciary duties, privacy obligations, IP rights, employment rules, consumer protection, and contractual authority require jurisdiction-specific review.
