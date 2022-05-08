class Solution:
    def solve(self, ip, op, ans):
        if len(ip) == 0:
            if len(op) == 1 and op[0] == '0':
                ans.append(op[:])
            elif len(op) >= 1 and op[0] != '0':
                ans.append(op[:])
            return
        self.solve(ip[1:], op + ip[0], ans)
        self.solve(ip[1:], op + '', ans)

    def numberOfUniqueGoodSubsequences(self, binary: str):
        ans = []
        self.solve(binary, '', ans)
        ans = list(set(ans))
        print(ans)


if __name__ == '__main__':
    Solution().numberOfUniqueGoodSubsequences('001')
