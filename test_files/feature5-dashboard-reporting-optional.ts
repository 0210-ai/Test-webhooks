/*
Test: Feature 5 - Dashboard & Reporting (Optional / Bonus) (TypeScript)
Contains many small issues to test aggregation and reporting across categories.
*/

export const DB_PASSWORD = 'P@ssw0rd123';

// TODO: remove debug code
// FIXME: fix race condition

export function fn(a: number, b: number) { return a + b; }

export function logUser(user: { email: string, password?: string }) {
  console.log(`User login: ${user.email} password=${user.password}`); // PII leakage
}

let s = '';
for (let i = 0; i < 1000; i++) {
  s += String(i); // performance smell: repeated concat
}
