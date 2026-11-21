# Independent Agent Emergency-Stop Requirements

**Status:** Requirements specification; not an implemented distributed kill switch.

## Objective

Provide an authorized human with a reliable way to stop agent activity across orchestration, tool execution, and provider integrations without relying on the agent to cooperate.

## Required properties

- **Out-of-band control:** the stop control is operated outside the agent process and outside its conversational authority.
- **Central policy:** tool gateways and execution workers check stop state before accepting new work and before consequential side effects.
- **Credential containment:** stop procedure can disable or revoke delegated credentials and short-lived tokens where supported.
- **Queue control:** queued jobs are paused or cancelled; in-flight operations are enumerated and handled according to their side-effect state.
- **Fail-closed behavior:** loss of the control-plane heartbeat or inability to verify policy blocks new consequential actions.
- **Human authority:** only named, authenticated operators may stop or resume a system.
- **Evidence:** record operator, timestamp, scope, reason, affected agents, in-flight jobs, and recovery approval.
- **Recovery gate:** resumption requires incident review, credential review, policy validation, and explicit authorization.

## Stop sequence

1. Deny new tool invocations at the gateway.
2. Pause schedulers and queued jobs.
3. Cancel in-flight work where cancellation is safe and supported.
4. Revoke or disable delegated credentials and sessions.
5. Block outbound actions at the egress boundary.
6. Preserve audit evidence and identify completed, partial, and uncertain side effects.
7. Notify authorized operators through an independent channel.

## Test cases

- Agent ignores stop instruction.
- Orchestrator becomes unavailable.
- Gateway loses connection to policy service.
- Provider API continues responding after local agent shutdown.
- Long-running job has already initiated an external side effect.
- Credentials remain valid after a worker is terminated.
- Stop command is issued while a human approval is pending.
- Recovery is attempted by an unauthorized identity.

## Acceptance criteria

A production system is not considered to have an independent kill switch until tests demonstrate that new consequential actions are blocked at every execution boundary, outstanding work is accounted for, and delegated credentials can be contained within documented provider limits.

## Important distinction

A local in-memory flag, agent prompt, UI pause button, or process termination is not sufficient evidence of a distributed emergency stop. Provider-specific behavior and credential revocation delays must be documented.
