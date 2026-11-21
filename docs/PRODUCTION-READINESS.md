# Agent Production Readiness Checklist

Use this checklist for one narrowly scoped workflow at a time. A pilot is not production-ready merely because a demo succeeds.

## Gate 0 — Ownership and authority

- [ ] Legal entity and accountable business owner identified.
- [ ] Human sponsor and approvers documented.
- [ ] IP, data rights, vendor terms, and permitted use reviewed.
- [ ] Public/private disclosure boundary approved.

## Gate 1 — Scope and data

- [ ] Single workflow and measurable outcome defined.
- [ ] Inputs, outputs, users, and excluded use cases documented.
- [ ] Data inventory and classification completed.
- [ ] Synthetic or approved test data available.
- [ ] Retention, deletion, and access rules documented.

## Gate 2 — Identity and permissions

- [ ] Agent has a stable technical identity.
- [ ] Sponsor and legal accountability are separately recorded.
- [ ] Least-privilege tool allowlist enforced at the tool boundary.
- [ ] Unknown tools and resources fail closed.
- [ ] Human approval required for consequential actions.
- [ ] Secrets are stored outside source control and prompts.

## Gate 3 — Security and resilience

- [ ] Threat model includes prompt injection and untrusted content.
- [ ] Egress and data-exfiltration controls tested.
- [ ] Sensitive-data handling and redaction tested.
- [ ] Independent emergency-stop behavior tested.
- [ ] Failure, timeout, retry, and duplicate-action behavior tested.
- [ ] Audit logs are access-controlled and tamper-evident.
- [ ] Incident and credential-revocation runbooks exist.

## Gate 4 — Quality and evaluation

- [ ] Representative evaluation set approved.
- [ ] Accuracy and task-completion thresholds defined.
- [ ] Regression tests run on every material change.
- [ ] Human review sampling and escalation path defined.
- [ ] Model fallback behavior tested.
- [ ] Accessibility and user experience reviewed where relevant.

## Gate 5 — Economics and operations

- [ ] Cost measured by project, agent, model, and user where supported.
- [ ] Hard spend controls and overage behavior verified with provider.
- [ ] Latency, error rate, and usage dashboards available.
- [ ] ROI baseline and measurement window documented.
- [ ] Support owner, operating hours, and service expectations set.

## Gate 6 — Controlled release

- [ ] Limited cohort and rollback plan approved.
- [ ] Production access explicitly authorized.
- [ ] Monitoring and incident response active.
- [ ] Review date and expansion criteria documented.
- [ ] No expansion without evidence from the previous gate.

**Release decision:** Hold until all mandatory controls are evidenced and the accountable owner approves the specific workflow.
