/*
Test: Feature 4 - Developer-Friendly Feedback (TypeScript)
Contains issues with inline EXPECTED FIX comments to validate that the guardrails provide actionable remediation.
*/

export function getUserByNameUnsafe(name: string) {
  // ISSUE: SQL injection via string formatting
  // EXPECTED FIX: Use parameterized queries (e.g., db.query('SELECT * FROM users WHERE name = $1', [name]))
  const query = `SELECT * FROM users WHERE name = '${name}'`;
  return query;
}

export const API_TOKEN = 'token-1234-SECRET';
// EXPECTED FIX: use process.env['API_TOKEN'] or a secret manager
