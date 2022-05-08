class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        t = [1 for _ in range(n+1)]

        for i in range(2, n+1):
            x = int(s[i - 2:i])
            if s[i - 1] == '0' and s[i - 2] == '0':
                t[i] = 0
            if s[i-1] != '0' and s[i-2] != '0':
                if x > 26:
                    t[i] = t[i-1]
                else:
                    t[i] = t[i-1] + t[i-2]
            if s[i-1] == '0' and s[i-2] != '0':
                if x > 26:
                    t[i] = 0
                else:
                    t[i] = t[i-2]
            if s[i-1] != '0' and s[i-2] == '0':
                t[i] = t[i-1]

        print(t)


if __name__ == '__main__':
    s = '27'
    Solution().numDecodings(s)