class Solution:
    def solve(self, s, i, s1, s2):
        if s1 == s1[::-1] and s2 == s2[::-1]:
            # print(s1, s2)
            self.ans = max(self.ans, len(s1) * len(s2))
        if i == len(s):
            return
        if (i, s1, s2) in self.d:
            return
        self.d.add((i, s1, s2))
        self.solve(s, i + 1, s1 + s[i], s2)
        self.solve(s, i + 1, s1, s2 + s[i])
        self.solve(s, i + 1, s1, s2)

    def maxProduct(self, s: str) -> int:
        self.ans = 0
        self.d = set()
        self.solve(s, 0, '', '')
        return self.ans
