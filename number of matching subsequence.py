class Solution:
    def isSubsequence(self, s: str, t: str):
        if len(s) == 0:
            return True
        i, j = 0, 0
        while i < len(t):
            if t[i] == s[j]:
                j = j + 1
                if j == len(s):
                    return 1
            i = i + 1
        return 0

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans, d = 0, {}
        for word in words:
            if word not in d:
                d[word] = self.isSubsequence(word, s)
            ans += d[word]
        return ans
