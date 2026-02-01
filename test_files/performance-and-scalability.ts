/*
Test: Performance & Scalability (TypeScript)
Includes O(n^2) patterns, blocking-like work, unbounded recursion, and inefficient string operations.
*/

export function duplicateWork(items: number[]) {
  const out: [number, number][] = [];
  for (const i of items) {
    for (const j of items) {
      if (i === j) {
        out.push([i, j]);
      }
    }
  }
  return out;
}

export function slowLoop(n: number) {
  const results: number[] = [];
  for (let i = 0; i < n; i++) {
    // Simulate heavy blocking CPU task
    const start = Date.now();
    while (Date.now() - start < 5) {
      // busy wait - blocks event loop
    }
    results.push(i);
  }
  return results;
}

export function recurse(n: number): number {
  if (n <= 0) return 0;
  return 1 + recurse(n - 1); // unbounded recursion can cause stack overflow
}
