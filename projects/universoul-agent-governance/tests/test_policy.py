import unittest

from universoul_guard.policy import (
    ActionRequest,
    DecisionStatus,
    PolicyConfig,
    PolicyEngine,
)


class PolicyEngineTests(unittest.TestCase):
    def setUp(self):
        self.engine = PolicyEngine(
            PolicyConfig(
                allowed_tools=frozenset({"read_public_file", "send_email"}),
                approval_required=frozenset({"send_email"}),
                denied_tools=frozenset({"delete_production_data"}),
            )
        )

    def request(self, tool):
        return ActionRequest(agent_id="test-agent", tool=tool)

    def test_allowlisted_low_risk_tool_is_allowed(self):
        result = self.engine.evaluate(self.request("read_public_file"))
        self.assertEqual(result.status, DecisionStatus.ALLOW)
        self.assertTrue(result.permitted_to_execute)

    def test_unknown_tool_is_denied(self):
        result = self.engine.evaluate(self.request("unknown_tool"))
        self.assertEqual(result.status, DecisionStatus.DENY)
        self.assertEqual(result.reason, "tool_not_allowlisted")

    def test_consequential_tool_requires_approval(self):
        result = self.engine.evaluate(self.request("send_email"))
        self.assertEqual(result.status, DecisionStatus.APPROVAL_REQUIRED)
        self.assertFalse(result.permitted_to_execute)

    def test_explicit_deny_overrides_allowlist(self):
        config = PolicyConfig(
            allowed_tools=frozenset({"delete_production_data"}),
            denied_tools=frozenset({"delete_production_data"}),
        )
        result = PolicyEngine(config).evaluate(self.request("delete_production_data"))
        self.assertEqual(result.status, DecisionStatus.DENY)

    def test_emergency_stop_denies_previously_allowed_tool(self):
        self.engine.stop()
        result = self.engine.evaluate(self.request("read_public_file"))
        self.assertEqual(result.status, DecisionStatus.DENY)
        self.assertEqual(result.reason, "emergency_stop_active")

    def test_resume_only_affects_local_engine_instance(self):
        self.engine.stop()
        self.engine.resume()
        result = self.engine.evaluate(self.request("read_public_file"))
        self.assertEqual(result.status, DecisionStatus.ALLOW)

    def test_missing_identity_is_denied(self):
        result = self.engine.evaluate(ActionRequest(agent_id="", tool="read_public_file"))
        self.assertEqual(result.status, DecisionStatus.DENY)
        self.assertEqual(result.reason, "missing_agent_or_tool")


if __name__ == "__main__":
    unittest.main()
