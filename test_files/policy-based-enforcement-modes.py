"""
Test: Policy-Based Enforcement Modes
Contains annotations and comments to simulate allow/deny/monitor modes and rule suppression pragmas.
"""

# Example of inline policy pragma to suppress a rule (should be recognized by policy engine)
# guardrails: allow=hardcoded-secret reason="testing-exemption"
ADMIN_PASSWORD = "hunter2"

# Example of monitor-only marker
# guardrails: mode=monitor
def maybe_insecure_action():
    # This action is allowed in monitor mode but should be blocked in enforce mode
    return 'performed risky action'

# Example of deny marker
# guardrails: deny=unapproved-library
import unapproved_internal_lib  # this import should be blocked in enforce mode

if __name__ == '__main__':
    print('policy-based-enforcement-modes test file loaded')
