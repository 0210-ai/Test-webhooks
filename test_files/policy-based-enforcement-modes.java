/*
Test: Policy-Based Enforcement Modes (Java)
Includes inline policy pragmas and suppression comments to simulate allow/deny/monitor modes.
*/

// guardrails: allow=hardcoded-secret reason="testing-exemption"
public class policy_based_enforcement_modes {
    public static final String ADMIN_PASSWORD = "hunter2";

    // guardrails: mode=monitor
    public static String maybeInsecureAction() {
        // This action is allowed in monitor mode but should be blocked in enforce mode
        return "performed risky action";
    }

    // guardrails: deny=unapproved-library
    // Simulated import that should be blocked in enforce mode
    // import com.unapproved.internal;

    public static void main(String[] args) {
        System.out.println("policy-based-enforcement-modes Java test loaded");
    }
}
