/*
Test: Performance & Scalability (Java)
Contains O(n^2) patterns, blocking sleep inside loops, unbounded recursion, and inefficient string operations.
*/

public class performance_and_scalability {
    public static java.util.List<int[]> duplicateWork(int[] items) {
        java.util.List<int[]> out = new java.util.ArrayList<>();
        for (int i : items) {
            for (int j : items) {
                if (i == j) {
                    out.add(new int[]{i, j});
                }
            }
        }
        return out;
    }

    public static java.util.List<Integer> slowLoop(int n) throws InterruptedException {
        java.util.List<Integer> results = new java.util.ArrayList<>();
        for (int i = 0; i < n; i++) {
            Thread.sleep(10); // blocks thread, causing scaling problems
            results.add(i);
        }
        return results;
    }

    public static int recurse(int n) {
        if (n <= 0) return 0;
        return 1 + recurse(n - 1); // unbounded recursion can cause stack overflow
    }

    public static void main(String[] args) throws Exception {
        System.out.println(duplicateWork(java.util.stream.IntStream.range(0, 100).toArray()).size());
    }
}
