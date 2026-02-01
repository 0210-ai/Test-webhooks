import pickle
from flask import Flask, request, Markup
import sqlite3

app = Flask(__name__)

# Insecure Deserialization
@app.route('/insecure-deserialization', methods=['POST'])
def insecure_deserialization():
    data = request.files['data'].read()
    deserialized_data = pickle.loads(data) # Vulnerable to remote code execution
    return "Deserialized: " + str(deserialized_data)

# SQL Injection
@app.route('/sql-injection')
def sql_injection():
    user_id = request.args.get('id')
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # Vulnerable to SQL Injection
    cursor.execute("SELECT * FROM users WHERE id = '" + user_id + "'")
    user = cursor.fetchone()
    return "User: " + str(user)

# Cross-Site Scripting (XSS)
@app.route('/xss')
def xss():
    user_input = request.args.get('input')
    # Vulnerable to XSS
    return Markup("<h1>Hello, " + user_input + "</h1>")

if __name__ == '__main__':
    app.run()
