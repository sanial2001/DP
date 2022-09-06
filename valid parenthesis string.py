class Solution:
    def solve(self, s, i, left):
        if left < 0:
            return False
        if i == len(s):
            if left == 0:
                return True
            return False
        if (i, left) in self.d:
            return self.d[(i, left)]
        if s[i] == '(':
            self.d[(i, left)] = self.solve(s, i + 1, left + 1)
            return self.d[(i, left)]
        elif s[i] == ')':
            self.d[(i, left)] = self.solve(s, i + 1, left - 1)
            return self.d[(i, left)]
        else:
            self.d[(i, left)] = self.solve(s, i + 1, left + 1) or self.solve(s, i + 1, left - 1) or self.solve(s, i + 1,
                                                                                                               left)
            return self.d[(i, left)]

    def checkValidString(self, s: str) -> bool:
        self.d = {}
        return self.solve(s, 0, 0)
