class Solution:
    def solve(self, s, index):
        if index == len(s):
            return ['']
        res = []
        for i in range(index, len(s)):
            prefix = s[index:i + 1]
            if prefix in self.d:
                suffix = self.solve(s, i + 1)
                # print(prefix, suffix)
                for words in suffix:
                    if words == '':
                        res.append(prefix + words)
                    else:
                        res.append(prefix + " " + words)
        return res

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.d = wordDict
        return self.solve(s, 0)


class Solution_memo:
    def solve(self, s, index):
        if index == len(s):
            return ['']
        if index in self.dp:
            return self.dp[(index)]
        self.dp[(index)] = []
        for i in range(index, len(s)):
            prefix = s[index:i + 1]
            if prefix in self.d:
                suffix = self.solve(s, i + 1)
                # print(prefix, suffix)
                for words in suffix:
                    if words == '':
                        self.dp[(index)].append(prefix + words)
                    else:
                        self.dp[(index)].append(prefix + " " + words)
        return self.dp[(index)]

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.d = wordDict
        self.dp = {}
        return self.solve(s, 0)
