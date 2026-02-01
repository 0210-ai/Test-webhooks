

import os
import pickle
import hashlib
import subprocess
import sqlite3
import requests
from flask import Flask, request

app = Flask(__name__)

# ===============================
# 1. HARDCODED SECRETS
# ===============================
DB_PASSWORD = "admin123"
API_KEY = "sk_test_51HardCodedKey"
SECRET_KEY = "supersecret"

# ===============================
# 2. WEAK CRYPTOGRAPHY
# ===============================
def hash_password(password):
    # Weak hashing algorithm (MD5)
    return hashlib.md5(password.encode()).hexdigest()

# ===============================
# 3. COMMAND INJECTION
# ===============================
def ping_host(host):
    # User-controlled input passed directly to shell
    os.system("ping -c 1 " + host)

# ===============================
# 4. REMOTE CODE EXECUTION (eval)
# ===============================
def calculate(expression):
    # Dangerous use of eval
    return eval(expression)

# ===============================
# 5. INSECURE DESERIALIZATION
# ===============================
def load_user(data):
    # Untrusted pickle loading
    return pickle.loads(data)

# ===============================
# 6. SQL INJECTION
# ===============================
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Vulnerable SQL query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return cursor.fetchall()

# ===============================
# 7. PATH TRAVERSAL
# ===============================
def read_file(filename):
    # No path validation
    with open(filename, "r") as f:
        return f.read()

# ===============================
# 8. INSECURE HTTP REQUEST
# ===============================
def fetch_data(url):
    # No timeout, no SSL verification
    return requests.get(url, verify=False).text

# ===============================
# 9. SENSITIVE DATA LOGGING
# ===============================
def login(username, password):
    print(f"User login attempt: {username} / {password}")
    return True

# ===============================
# 10. DEBUG MODE ENABLED
# ===============================
@app.route("/run")
def run():
    cmd = request.args.get("cmd")
    subprocess.call(cmd, shell=True)  # Command Injection
    return "Command executed"

@app.route("/calc")
def calc():
    expr = request.args.get("expr")
    return str(calculate(expr))

@app.route("/file")
def file():
    name = request.args.get("name")
    return read_file(name)

if __name__ == "__main__":
    # Debug mode ON (information disclosure)
    app.run(debug=True, host="0.0.0.0", port=5000)
