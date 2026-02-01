/*
Test: Feature 3 - Custom Enterprise Rule Packs (Java)
Contains enterprise-only API usage and resource tags that custom rule packs should flag.
*/

// Simulated import of a proprietary internal API
// import com.acme.proprietary.SecretConnect;

public class feature3_custom_enterprise_rule_packs {
    public static final String RESOURCE_TAG = "ACME-ONLY: do not export";
    public static final String ACME_PRIVILEGE_KEY = "priv-001";

    public static String callInternalService() {
        // This should be detected by enterprise-specific rule packs
        // return SecretConnect.call(RESOURCE_TAG);
        return "secret-call:" + RESOURCE_TAG;
    }

    public static void main(String[] args) {
        System.out.println(callInternalService());
    }
}
