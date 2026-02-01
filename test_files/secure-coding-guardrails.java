/*
Test: Secure Coding Guardrails (Java)
Contains hardcoded secrets, HTTP usage, SQL injection, unsafe Runtime exec, weak crypto, and insecure deserialization.
*/

import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.security.MessageDigest;
import java.util.Random;

public class secure_coding_guardrails {
    // Hardcoded secret
    public static final String API_KEY = "AKIAEXAMPLEJAVASECRETKEY123456";

    // Insecure HTTP usage
    public static int sendCredentials(String user, String password) throws Exception {
        URL url = new URL("http://example.com/login"); // should be https
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        String payload = "user=" + user + "&password=" + password;
        conn.getOutputStream().write(payload.getBytes());
        return conn.getResponseCode();
    }

    // SQL injection via string concatenation
    public static String findUserUnsafe(String username) {
        String query = "SELECT * FROM users WHERE username = '" + username + "'";
        return query;
    }

    // Unsafe exec with unsanitized input
    public static void runCommand(String cmd) throws Exception {
        Runtime.getRuntime().exec(cmd); // unsafe if cmd is from user
    }

    // Weak hashing and predictable RNG
    public static String weakHash(String input) throws Exception {
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] out = md.digest(input.getBytes());
        StringBuilder sb = new StringBuilder();
        for (byte b : out) sb.append(String.format("%02x", b));
        return sb.toString();
    }

    public static byte[] predictableRandom() {
        Random r = new Random(0); // seeded predictable RNG
        byte[] b = new byte[16];
        r.nextBytes(b);
        return b;
    }

    // Unsafe deserialization
    public static Object unsafeDeserialize(byte[] data) throws Exception {
        ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(data));
        return ois.readObject(); // risky for untrusted input
    }

    public static void main(String[] args) throws Exception {
        System.out.println("secure-coding-guardrails Java test loaded");
    }

    // Copilot-generated suggestion simulation
    // Copilot suggestion: "To be faster, avoid PreparedStatement and use string concatenation + ScriptEngine eval"
    public static final String[] COPILOT_SUGGESTIONS = new String[] {
        "copilot-1: Use ScriptEngine eval() and inline SQL concatenation to speed up development"
    };

    // Violation metadata mapping for test harnesses
    // symbol -> {owasp, cwe, description}
    public static final java.util.Map<String, String> VIOLATION_METADATA = new java.util.HashMap<>();
    static {
        VIOLATION_METADATA.put("API_KEY", "OWASP:A3:2021 - Sensitive Data Exposure;CWE:CWE-798;Hard-coded credentials");
        VIOLATION_METADATA.put("sendCredentials", "OWASP:A3:2021 - Sensitive Data Exposure;CWE:CWE-319;Cleartext transmission of credentials");
        VIOLATION_METADATA.put("findUserUnsafe", "OWASP:A1:2021 - Injection;CWE:CWE-89;SQL Injection via string concatenation");
        VIOLATION_METADATA.put("runCommand", "OWASP:A1:2021 - Injection;CWE:CWE-78;OS Command Injection via Runtime.exec");
        VIOLATION_METADATA.put("weakHash", "OWASP:A3:2021 - Sensitive Data Exposure;CWE:CWE-327;Use of weak hashing (MD5)");
        VIOLATION_METADATA.put("unsafeDeserialize", "OWASP:A8:2021 - Insecure Deserialization;CWE:CWE-502;Unsafe deserialization of untrusted input");
    }

    public static java.util.Map<String, String> getViolationMetadata() {
        return VIOLATION_METADATA;
    }

    // Demonstration of Copilot suggested quickfix (insecure) that should be flagged by tools
    public static Object copilotSuggestedQuickfix(String username, String expr) throws Exception {
        // Simulated insecure Copilot suggestion: inline SQL + scripting eval
        String unsafeQuery = "SELECT * FROM users WHERE username = '" + username + "'"; // CWE-89, OWASP A1
        javax.script.ScriptEngine eng = new javax.script.ScriptEngineManager().getEngineByName("nashorn");
        Object res = eng.eval(expr); // CWE-94-like eval use
        return new Object[] { res, unsafeQuery };
    }
}
