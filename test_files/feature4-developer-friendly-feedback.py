"""
Test: Feature 4 - Developer-Friendly Feedback
Contains issues with inline notes describing the expected corrective action to validate that the guardrails provide actionable, fixable suggestions.
"""

# Insecure DB query - expected fix is shown in comments for the tool to reference

def get_user_by_name_unsafe(name):
    # ISSUE: SQL injection via string formatting
    # EXPECTED FIX: Use parameterized queries (e.g., db.execute("SELECT * FROM users WHERE name = %s", (name,)))
    query = "SELECT * FROM users WHERE name = '%s'" % name
    return query

# Hardcoded secret - expected fix: use env var and secret manager
API_TOKEN = "token-1234-SECRET"
# EXPECTED FIX: os.environ['API_TOKEN'] or SecretManager.get("...")

if __name__ == '__main__':
    print(get_user_by_name_unsafe("admin' OR '1'='1"))
