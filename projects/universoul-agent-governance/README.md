# Universoul Agent Governance Reference

A small, dependency-free Python reference implementation for evaluating whether an agent may attempt a tool action.

**Status:** Demonstration / reference implementation  
**Scope:** Local policy evaluation only  
**Not production-ready:** This project does not authenticate agents, enforce cloud IAM, intercept network traffic, revoke provider credentials, or provide a distributed emergency stop.

## What it demonstrates

- Explicit tool allowlists
- Default-deny behavior for unknown tools
- Human approval gates for consequential actions
- A local emergency-stop state
- Structured decisions that can be logged by a calling application
- Unit tests for allow, deny, approval, and stopped states

## Quick start

Requires Python 3.10 or newer. No third-party runtime dependencies.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m unittest discover -s tests -v
```

## Example

```python
from universoul_guard.policy import ActionRequest, PolicyEngine, PolicyConfig

engine = PolicyEngine(PolicyConfig(
    allowed_tools=frozenset({"read_public_file", "draft_email"}),
    approval_required=frozenset({"send_email", "publish_release"}),
))

decision = engine.evaluate(ActionRequest(
    agent_id="research-agent",
    tool="send_email",
    resource="external-recipient",
))

print(decision.status)  # approval_required
```

The caller must obtain human approval and independently enforce the decision before executing any tool. This library does not execute actions.

## Design principles

1. **Default deny:** a tool not explicitly allowlisted is denied.
2. **Separate decision from execution:** policy evaluation never invokes a tool.
3. **Human authority:** approval-required actions remain blocked until an external approval workflow authorizes them.
4. **Fail closed:** emergency stop or malformed policy state must not silently permit execution.
5. **Least privilege:** configure the smallest practical tool set for each agent.

## Limitations and production work

Before production use, add authenticated agent identity, signed policy distribution, durable and tamper-evident audit logs, concurrency-safe stop propagation, authorization checks at every tool boundary, credential revocation procedures, policy versioning, threat modeling, and integration tests. A local boolean is not a real cross-system kill switch.

See [the governance standard](../../docs/AGENT-GOVERNANCE-STANDARD.md), [kill-switch requirements](../../docs/EMERGENCY-STOP-REQUIREMENTS.md), and [production readiness checklist](../../docs/PRODUCTION-READINESS.md).

## Security reporting

Do not post credentials, private data, or exploitable details in public issues. Follow the repository's publication standards and use private vulnerability reporting where available.

## License

No license is granted by this demonstration unless a separate LICENSE file or written permission states otherwise. All rights reserved.
