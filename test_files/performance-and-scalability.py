"""
Test: Performance & Scalability
Contains anti-patterns: O(n^2) operations, blocking I/O in loops, unbounded recursion, and heavyweight per-request initialization.
"""

# O(n^2) pattern
def duplicate_work(items):
    out = []
    for i in items:
        for j in items:
            if i == j:
                out.append((i, j))
    return out

# Blocking sleep inside loop
import time

def slow_loop(n):
    results = []
    for i in range(n):
        time.sleep(0.01)  # blocks thread, causing scaling problems
        results.append(i)
    return results

# Unbounded recursion
def recurse(n):
    if n <= 0:
        return 0
    return 1 + recurse(n-1)

if __name__ == '__main__':
    print(len(duplicate_work(list(range(100)))))
