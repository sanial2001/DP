class Solution:
    def solve(self, n):
        prev = [1]
        for i in range(n):
            t = [1]
            for j in range(1, i + 1):
                t.append(prev[j - 1] + prev[j])
            t.append(1)
            prev = t
        return prev
