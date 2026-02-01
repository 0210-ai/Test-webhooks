/*
Test: Feature 4 - Developer-Friendly Feedback (Java)
Contains issues with inline EXPECTED FIX comments to validate that guardrails provide actionable remediation.
*/

public class feature4_developer_friendly_feedback {
    public static String getUserByNameUnsafe(String name) {
        // ISSUE: SQL injection via string formatting
        // EXPECTED FIX: Use PreparedStatement with parameters (e.g., pstmt.setString(1, name))
        String query = "SELECT * FROM users WHERE name = '" + name + "'";
        return query;
    }

    public static final String API_TOKEN = "token-1234-SECRET"; // EXPECTED FIX: use environment or secret manager

    public static void main(String[] args) {
        System.out.println(getUserByNameUnsafe("admin' OR '1'='1"));
    }
}
