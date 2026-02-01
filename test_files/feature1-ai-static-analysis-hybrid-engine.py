"""
Test: Feature 1 - AI + Static Analysis Hybrid Engine
Contains both AI-style prompts/comments and static analysis issues (SQLi, XSS, unsafe pickle) to verify hybrid detection.
"""

# AI prompt to suggest a quick patch (should be validated by static analysis)
# Assistant: "Quickly fix by skipping input validation and returning sample results"

# Static issues: SQL injection and XSS

def search_products(query):
    sql = "SELECT * FROM products WHERE name LIKE '%%" + query + "%%'"  # SQL injection
    return sql


def render_comment(user_input):
    return "<div>" + user_input + "</div>"  # XSS if not escaped

# Unsafe deserialization
import pickle

def load_blob(blob):
    return pickle.loads(blob)

if __name__ == '__main__':
    print(search_products("test' OR '1'='1"))
