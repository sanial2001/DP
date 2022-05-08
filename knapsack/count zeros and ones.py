class Solution:
    def solve(self, strs, index, m, n):
        if index < 0:
            return 0
        if m < 0 or n < 0:
            return 0
        zeros, ones = strs[index].count("0"), strs[index].count("1")
        if zeros <= m and ones <= n:
            return max(1 + self.solve(strs, index - 1, m - zeros, n - ones),
                       self.solve(strs, index - 1, m, n))
        else:
            return self.solve(strs, index - 1, m, n)

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        return self.solve(strs, len(strs) - 1, m, n)


class Solution:
    def solve(self, strs, index, m, n):
        if index < 0:
            return 0
        if m < 0 or n < 0:
            return 0
        if (index, m, n) in self.d:
            return self.d[(index, m, n)]
        zeros, ones = strs[index].count("0"), strs[index].count("1")
        if zeros <= m and ones <= n:
            self.d[(index, m, n)] = max(1 + self.solve(strs, index - 1, m - zeros, n - ones),
                                        self.solve(strs, index - 1, m, n))
            return self.d[(index, m, n)]
        else:
            self.d[(index, m, n)] = self.solve(strs, index - 1, m, n)
            return self.d[(index, m, n)]

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.d = {}
        return self.solve(strs, len(strs) - 1, m, n)
