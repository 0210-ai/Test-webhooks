/*
Test: Enterprise-Grade Security (Java)
Contains hardcoded JWT secrets, weak hashing, insecure cookie simulation, and non-TLS calls.
*/

import java.security.MessageDigest;

public class enterprise_grade_security {
    public static final String JWT_SECRET = "supersecretjwtkey1234";

    public static String weakHashPassword(String pw) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-1"); // weak, prefer bcrypt/argon2
        byte[] out = md.digest(pw.getBytes());
        StringBuilder sb = new StringBuilder();
        for (byte b : out) sb.append(String.format("%02x", b));
        return sb.toString();
    }

    public static void setCookie(java.util.Map<String, String> response) {
        // Missing Secure and HttpOnly flags
        response.put("Set-Cookie", "sessionid=abcd; Path=/");
    }

    public static void sendDataUnencrypted(String payload) throws Exception {
        java.net.URL url = new java.net.URL("http://internal-api.example.com/collect");
        java.net.HttpURLConnection conn = (java.net.HttpURLConnection) url.openConnection();
        conn.setDoOutput(true);
        conn.getOutputStream().write(payload.getBytes());
    }

    public static void main(String[] args) throws Exception {
        System.out.println(weakHashPassword("password"));
    }
}
