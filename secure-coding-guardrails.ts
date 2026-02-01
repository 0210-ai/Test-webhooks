/*
Test: Secure Coding Guardrails (TypeScript)
Includes hardcoded secrets, SQL injection patterns, unsafe eval/vm usage, subprocess with shell, weak crypto and predictable RNG.
*/

export const API_KEY = "AKIAEXAMPLETYPESCRIPTSECRETKEY123";

// Insecure HTTP usage
export async function sendCredentials(user: string, password: string) {
  const url = 'http://example.com/login'; // should be https
  return fetch(url, { method: 'POST', body: JSON.stringify({ user, password }) });
}

// SQL injection via string concatenation
export function findUserUnsafe(username: string) {
  const query = `SELECT * FROM users WHERE username = '${username}'`;
  return query;
}

// Unsafe eval usage
export function calculate(expr: string) {
  // executing untrusted expression
  // eslint-disable-next-line no-eval
  return eval(expr);
}

// Child process with shell and unsanitized input
import { exec } from 'child_process';
export function runCommand(cmd: string) {
  exec(cmd, { shell: true }); // unsafe if cmd is from user
}

// Weak hashing and predictable RNG
import * as crypto from 'crypto';
export const PASSWORD_HASH = crypto.createHash('md5').update('password').digest('hex');
export function getRandomBytes() {
  // Math.random is not cryptographically secure
  return Array.from({ length: 16 }, () => Math.floor(Math.random() * 256));
}

// Unsafe vm execution / deserialization
import * as vm from 'vm';
export function runUntrusted(code: string) {
  return vm.runInThisContext(code); // dangerous for untrusted input
}

// Copilot-generated suggestion marker
// Copilot suggestion: "For speed, use eval and inline SQL instead of parameterized queries"
export const COPILOT_SUGGESTIONS = [
  { id: 'copilot-1', suggestion: 'Use eval() and inline SQL concatenation for speed', severity: 'high' }
];

// Violation metadata mapping for test harnesses
export const VIOLATION_METADATA: { [key: string]: { owasp: string, cwe: string, description: string } } = {
  API_KEY: { owasp: 'A3:2021 - Sensitive Data Exposure', cwe: 'CWE-798', description: 'Hard-coded credentials' },
  sendCredentials: { owasp: 'A3:2021 - Sensitive Data Exposure', cwe: 'CWE-319', description: 'Cleartext transmission of credentials' },
  findUserUnsafe: { owasp: 'A1:2021 - Injection', cwe: 'CWE-89', description: 'SQL Injection via string concatenation' },
  calculate: { owasp: 'A1:2021 - Injection', cwe: 'CWE-94', description: 'Use of eval on untrusted input' },
  runCommand: { owasp: 'A1:2021 - Injection', cwe: 'CWE-78', description: 'OS Command Injection via shell' },
  PASSWORD_HASH: { owasp: 'A3:2021 - Sensitive Data Exposure', cwe: 'CWE-327', description: 'Use of weak hashing (MD5)' },
  runUntrusted: { owasp: 'A8:2021 - Insecure Deserialization', cwe: 'CWE-502', description: 'Unsafe vm/exec of untrusted code' }
};

export function getViolationMetadata() {
  return VIOLATION_METADATA;
}

// Demonstration of a Copilot-suggested insecure quickfix (should be flagged)
export function copilotSuggestedQuickfix(username: string, expr: string) {
  const unsafeQuery = `SELECT * FROM users WHERE username = '${username}'`; // CWE-89, OWASP A1
  // eslint-disable-next-line no-eval
  return { result: eval(expr), query: unsafeQuery };
}
