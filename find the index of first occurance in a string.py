class Solution:
    def solve(self, word1, word2, M, N):
        t = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
        for i in range(M + 1):
            for j in range(N + 1):
                if i == 0 or j == 0:
                    t[i][j] = 0

        for m in range(1, M + 1):
            for n in range(1, N + 1):
                if word1[m - 1] == word2[n - 1]:
                    t[m][n] = t[m - 1][n - 1] + 1
                else:
                    t[m][n] = 0

        res = max(max(i) for i in t)
        return res

    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if m < n:
            return -1
        val = self.solve(haystack, needle, m, n)
        # print(val)
        if val == n:
            for i in range(m):
                if haystack[i] == needle[0] and haystack[i:min(i + n, m)] == needle:
                    return i
        return -1
