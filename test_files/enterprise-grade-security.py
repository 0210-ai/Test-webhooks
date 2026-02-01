"""
Test: Enterprise-Grade Security
Contains patterns that should be caught by enterprise-grade checks: hardcoded JWT secrets, weak hashing, missing TLS, insecure cookies.
"""

# Hardcoded JWT secret
JWT_SECRET = "supersecretjwtkey1234"

# Weak password hashing
import hashlib
def weak_hash_password(pw):
    return hashlib.sha1(pw.encode()).hexdigest()  # should use bcrypt/argon2

# Simulated insecure cookie settings
def set_cookie(response):
    # Missing Secure and HttpOnly flags
    response['Set-Cookie'] = "sessionid=abcd; Path=/"

# Insecure use of HTTP endpoint
def send_data_unencrypted(payload):
    import requests
    requests.post('http://internal-api.example.com/collect', json=payload)

if __name__ == '__main__':
    print(weak_hash_password('password'))
