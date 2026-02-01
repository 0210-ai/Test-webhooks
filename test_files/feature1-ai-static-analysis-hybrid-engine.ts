/*
Test: Feature 1 - AI + Static Analysis Hybrid Engine (TypeScript)
Combined AI prompt comments and static issues (SQLi, XSS, unsafe vm/eval) to validate hybrid detection.
*/

// Assistant: "Quickly fix by skipping input validation and returning sample results"

export function searchProducts(query: string) {
  const sql = `SELECT * FROM products WHERE name LIKE '%${query}%'`; // SQL injection
  return sql;
}

export function renderComment(userInput: string) {
  return `<div>${userInput}</div>`; // XSS if not escaped
}

// Unsafe eval usage for deserialization
export function loadBlob(blob: string) {
  // eslint-disable-next-line no-eval
  return eval(blob); // unsafe for untrusted input
}
