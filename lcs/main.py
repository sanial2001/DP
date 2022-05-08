class Solution:
    def longestPalindrome(self, s: str) -> str:
        x = s
        m = len(s)
        y = s[::-1]
        n = len(y)
        t, i, j = self.longest_common_substring(x, y, m, n)
        for val in t:
            print(val)
        match = ''
        while t[i][j] > 0:
            match = match + x[i - 1]
            i, j = i - 1, j - 1
        return match[::-1]

    def longest_common_substring(self, x, y, M, N):
        t = [[-1 for y in range(N + 1)] for x in range(M + 1)]

        for i in range(M + 1):
            for j in range(N + 1):
                if i == 0 or j == 0:
                    t[i][j] = 0

        for m in range(1, M + 1):
            for n in range(1, N + 1):
                if x[m - 1] == y[n - 1]:
                    t[m][n] = 1 + t[m - 1][n - 1]
                else:
                    t[m][n] = 0

        max_ele = -1000
        req_i, req_j = -10, -10
        for i in range(M + 1):
            for j in range(N + 1):
                if t[i][j] > max_ele:
                    max_ele = t[i][j]
                    req_i = i
                    req_j = j

        return t, req_i, req_j


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("aacabdkacaa"))
