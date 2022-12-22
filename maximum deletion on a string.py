class Solution:
    def solve(self, s, index):
        n = len(s)
        if index == len(s):
            return 0
        if index in self.d:
            return self.d[index]
        res = 0
        for i in range(index, (index + n) // 2):
            # print(s[index:i+1], s[i+1:min(n, i+1 + i-index+1)])
            if s[index:i + 1] == s[i + 1:min(n, i + 1 + i - index + 1)]:
                res = max(res, self.solve(s, i + 1))
        self.d[index] = res + 1
        return self.d[index]

    def deleteString(self, s: str) -> int:
        self.d = {}
        return self.solve(s, 0)
