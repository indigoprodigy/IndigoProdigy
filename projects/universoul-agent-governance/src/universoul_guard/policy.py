"""Fail-closed policy evaluation for agent tool actions.

This module evaluates requests only. It never executes tools or grants credentials.
The calling application is responsible for enforcing every returned decision.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import FrozenSet, Optional


class DecisionStatus(str, Enum):
    ALLOW = "allow"
    DENY = "deny"
    APPROVAL_REQUIRED = "approval_required"


@dataclass(frozen=True)
class ActionRequest:
    agent_id: str
    tool: str
    resource: str = ""
    purpose: str = ""


@dataclass(frozen=True)
class PolicyConfig:
    allowed_tools: FrozenSet[str] = field(default_factory=frozenset)
    approval_required: FrozenSet[str] = field(default_factory=frozenset)
    denied_tools: FrozenSet[str] = field(default_factory=frozenset)


@dataclass(frozen=True)
class PolicyDecision:
    status: DecisionStatus
    reason: str
    agent_id: str
    tool: str
    resource: str = ""

    @property
    def permitted_to_execute(self) -> bool:
        """True only for an explicit allow decision."""
        return self.status is DecisionStatus.ALLOW


class PolicyEngine:
    """Evaluate actions using explicit allowlists and a local stop state."""

    def __init__(self, config: PolicyConfig) -> None:
        self._config = config
        self._stopped = False

    @property
    def stopped(self) -> bool:
        return self._stopped

    def stop(self) -> None:
        """Block all future requests evaluated by this engine instance."""
        self._stopped = True

    def resume(self) -> None:
        """Resume this local instance; production systems need stronger controls."""
        self._stopped = False

    def evaluate(self, request: ActionRequest) -> PolicyDecision:
        """Return a decision; never execute the requested action."""
        if not request.agent_id.strip() or not request.tool.strip():
            return self._decision(
                DecisionStatus.DENY, "missing_agent_or_tool", request
            )

        if self._stopped:
            return self._decision(DecisionStatus.DENY, "emergency_stop_active", request)

        if request.tool in self._config.denied_tools:
            return self._decision(DecisionStatus.DENY, "explicitly_denied", request)

        if request.tool not in self._config.allowed_tools:
            return self._decision(DecisionStatus.DENY, "tool_not_allowlisted", request)

        if request.tool in self._config.approval_required:
            return self._decision(
                DecisionStatus.APPROVAL_REQUIRED, "human_approval_required", request
            )

        return self._decision(DecisionStatus.ALLOW, "explicitly_allowlisted", request)

    @staticmethod
    def _decision(
        status: DecisionStatus, reason: str, request: ActionRequest
    ) -> PolicyDecision:
        return PolicyDecision(
            status=status,
            reason=reason,
            agent_id=request.agent_id,
            tool=request.tool,
            resource=request.resource,
        )
