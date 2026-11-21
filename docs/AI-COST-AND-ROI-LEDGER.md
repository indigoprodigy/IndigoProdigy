# AI Cost and ROI Ledger

A provider-neutral data model for measuring agent economics. This is a proposed ledger schema, not a live billing integration.

## Minimum event fields

| Field | Description |
|---|---|
| event_id | Unique usage event |
| occurred_at | UTC timestamp |
| legal_entity | Entity responsible for the workload |
| project_id | Approved project or cost center |
| agent_id | Stable agent registry ID |
| user_id | Pseudonymous internal user ID where appropriate |
| provider | Model or tool provider |
| model | Exact model identifier |
| input_units | Provider-reported input tokens or units |
| output_units | Provider-reported output tokens or units |
| tool_calls | Number and type of tool calls |
| duration_ms | End-to-end duration |
| cost_amount | Provider-reported or reconciled cost |
| currency | ISO currency code |
| outcome | Success, failure, partial, or human-escalated |
| value_metric | Workflow-specific measurable output |
| policy_version | Policy version used for the run |

## Controls

- Reconcile usage events to provider invoices.
- Separate estimates from billed amounts.
- Attribute shared infrastructure costs using a documented allocation rule.
- Do not assume project-level budget limits equal per-agent hard caps.
- Test provider cap behavior, latency, long-running jobs, and overage treatment.
- Use pseudonymous user identifiers unless identity is operationally necessary.
- Keep financial records in approved systems, not public repositories.

## ROI method

For each workflow, define a baseline before launch. Measure:

- Human time saved, net of review and correction time.
- Cost per successfully completed task.
- Error and rework rate.
- Throughput and cycle time.
- Incremental revenue or avoided cost, where verifiable.
- Risk and quality impacts.

Do not count gross model output or unverified time savings as realized value. Report assumptions and confidence separately.
