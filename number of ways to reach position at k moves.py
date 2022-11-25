class Solution:
    def dfs(self, s, e, k):
        if k == 0:
            if s == e:
                return 1
            return 0
        return self.dfs(s + 1, e, k - 1) + self.dfs(s - 1, e, k - 1)

    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        return self.dfs(startPos, endPos, k) % (10 ** 9 + 7)


class Solution:
    def dfs(self, s, e, k):
        if k == 0:
            if s == e:
                return 1
            return 0
        if (s, k) in self.d:
            return self.d[(s, k)]
        self.d[(s, k)] = self.dfs(s + 1, e, k - 1) + self.dfs(s - 1, e, k - 1)
        return self.d[(s, k)]

    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        self.d = {}
        return self.dfs(startPos, endPos, k) % (10 ** 9 + 7)
