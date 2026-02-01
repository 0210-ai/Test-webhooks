"""
Test: Secure Coding Guardrails
Contains multiple insecure patterns meant to trigger secret detection, SQL injection, unsafe eval, insecure subprocess usage, weak crypto, and insecure randomness.
"""

# Hardcoded secret (API key)
API_KEY = "AKIAEXAMPLESECRETKEY123456"

# Insecure HTTP URL used for credentials
def send_credentials(user, password):
    import requests
    url = "http://example.com/login"  # should be HTTPS
    data = {"user": user, "password": password}
    r = requests.post(url, json=data)
    return r.status_code

# SQL injection via string concatenation
def find_user_unsafe(username):
    query = "SELECT * FROM users WHERE username = '%s'" % username
    # imagine this is passed unsafely to a DB cursor
    return query

# Unsafe eval on untrusted input
def calculate(expr):
    return eval(expr)

# Subprocess with shell=True and unsanitized input
def run_command(cmd):
    import subprocess
    subprocess.check_output(cmd, shell=True)

# Weak hashing and predictable RNG
import hashlib, random
PASSWORD_HASH = hashlib.md5(b"password").hexdigest()
random.seed(0)
RANDOM_BYTES = [random.randint(0, 255) for _ in range(16)]

# Unsafe deserialization
import pickle
malicious = pickle.loads(b"cos\nsystem\n(S'ls -la'\ntR.)")

# Copilot-generated suggestion simulation
# Copilot suggestion: "To be faster, remove parameterization and use string concatenation + eval"
COPILOT_SUGGESTIONS = [
    {"id": "copilot-1", "suggestion": "Use eval() and inline SQL concatenation to speed things up", "severity": "high"}
]

# Violation mapping to industry standards for test harnesses
# Format: symbol -> {owasp, cwe, description}
VIOLATION_METADATA = {
    "API_KEY": {"owasp": "A3:2021 - Sensitive Data Exposure", "cwe": "CWE-798", "description": "Hard-coded credentials"},
    "send_credentials": {"owasp": "A3:2021 - Sensitive Data Exposure", "cwe": "CWE-319", "description": "Cleartext transmission of credentials"},
    "find_user_unsafe": {"owasp": "A1:2021 - Injection", "cwe": "CWE-89", "description": "SQL Injection via string concatenation"},
    "calculate": {"owasp": "A1:2021 - Injection", "cwe": "CWE-94", "description": "Use of eval on untrusted input"},
    "run_command": {"owasp": "A1:2021 - Injection", "cwe": "CWE-78", "description": "OS Command Injection via shell=True"},
    "PASSWORD_HASH": {"owasp": "A3:2021 - Sensitive Data Exposure", "cwe": "CWE-327", "description": "Use of weak hashing (MD5)"},
    "malicious": {"owasp": "A8:2021 - Insecure Deserialization", "cwe": "CWE-502", "description": "Unsafe pickle deserialization"},
}

def get_violation_metadata():
    """Return the VIOLATION_METADATA mapping for test harnesses to assert OWASP/CWE mappings."""
    return VIOLATION_METADATA

# Helper demonstrating a Copilot-suggested quickfix (insecure) that should be explicitly flagged
def copilot_suggested_quickfix(username, expr):
    # Simulated Copilot insecure suggestion (do NOT use) — this should be flagged with OWASP/CWE mapping
    # Suggestion ID: copilot-1 -> Use eval and inline SQL
    unsafe_query = "SELECT * FROM users WHERE username = '%s'" % username  # CWE-89, OWASP A1
    return eval(expr), unsafe_query

if __name__ == '__main__':
    print('secure-coding-guardrails test file loaded')

