class Solution:
    def check(self, x, y):
        m, n = len(x), len(y)
        if m - n > 1: return False
        i, j = 0, 0
        while i < m and j < n:
            if x[i] == y[j]:
                i, j = i + 1, j + 1
            else:
                i += 1
        return True if j == n else False

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        n = len(words)
        t = [1 for _ in range(n)]
        for i in range(n):
            j = i - 1
            temp = []
            while j >= 0:
                if self.check(words[i], words[j]):
                    temp.append(t[j])
                j -= 1
            if temp: t[i] = max(temp) + 1
        # print(words, t)
        return max(t)
