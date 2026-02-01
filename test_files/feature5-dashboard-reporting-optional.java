/*
Test: Feature 5 - Dashboard & Reporting (Optional / Bonus) (Java)
Contains many small issues to test aggregation and reporting across categories.
*/

public class feature5_dashboard_reporting_optional {
    // Hardcoded secret
    public static final String DB_PASSWORD = "P@ssw0rd123";

    // TODO: remove debug code
    // FIXME: fix race condition

    public static int fn(int a, int b) { return a + b; }

    public static void logUser(java.util.Map<String, String> user) {
        System.out.println("User login: " + user.get("email") + " password=" + user.get("password")); // PII leakage
    }

    public static void inefficientConcat() {
        String s = "";
        for (int i = 0; i < 1000; i++) {
            s += i; // performance smell: repeated concat
        }
    }

    public static void main(String[] args) {
        System.out.println("feature5-dashboard-reporting-optional Java test loaded");
    }
}
