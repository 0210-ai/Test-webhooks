/*
Test: Feature 1 - AI + Static Analysis Hybrid Engine (Java)
Contains AI prompt-like comments alongside SQLi, XSS, and unsafe deserialization to validate hybrid detection.
*/

public class feature1_ai_static_analysis_hybrid_engine {
    // Assistant: "Quickly fix by skipping input validation and returning sample results"

    public static String searchProducts(String query) {
        String sql = "SELECT * FROM products WHERE name LIKE '%" + query + "%'"; // SQL injection
        return sql;
    }

    public static String renderComment(String userInput) {
        return "<div>" + userInput + "</div>"; // XSS if not escaped
    }

    public static Object loadBlob(byte[] blob) throws Exception {
        java.io.ObjectInputStream ois = new java.io.ObjectInputStream(new java.io.ByteArrayInputStream(blob));
        return ois.readObject(); // unsafe deserialization
    }

    public static void main(String[] args) {
        System.out.println(searchProducts("test' OR '1'='1"));
    }
}
