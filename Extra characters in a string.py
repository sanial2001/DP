class Solution:
    def solve(self, s, index, dictionary, d):
        if index == len(s):
            return 0
        if index in d:
            return d[index]
        res = float("inf")
        for i in range(index, len(s)):
            word = s[index:i + 1]
            if word in dictionary:
                res = min(res, 0 + self.solve(s, i + 1, dictionary, d))
            else:
                res = min(res, len(word) + self.solve(s, i + 1, dictionary, d))
        d[index] = res
        return d[index]

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        d = {}
        return self.solve(s, 0, dictionary, d)
