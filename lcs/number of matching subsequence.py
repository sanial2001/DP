class Solution:
    def lcs(self, x, y, M, N):
        t = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
        for m in range(1, M + 1):
            for n in range(1, N + 1):
                if x[m - 1] == y[n - 1]:
                    t[m][n] = 1 + t[m - 1][n - 1]
                else:
                    t[m][n] = max(t[m][n - 1], t[m - 1][n])
        return t[M][N]

    def numMatchingSubseq(self, s: str, words) -> int:
        ans = 0
        for word in words:
            if self.lcs(s, word, len(s), len(word)) == len(word):
                ans += 1
        return ans


if __name__ == '__main__':
    s = "abcde"
    words = ["a", "bb", "acd", "ace"]
    print(Solution().numMatchingSubseq(s, words))
