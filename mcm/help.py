class Solution:
    def lcs_sol(self, x, y, s1, s2):
        t = [[-1 for _ in range(y + 1)] for _ in range(x + 1)]

        for i in range(x + 1):
            t[i][0] = 0
        for i in range(y + 1):
            t[0][i] = 0

        for X in range(1, x + 1):
            for Y in range(1, y + 1):
                if s1[X - 1] == s2[Y - 1]:
                    t[X][Y] = 1 + t[X - 1][Y - 1]
                else:
                    t[X][Y] = max(t[X][Y - 1], t[X - 1][Y])

        return t[x][y]

    def lcs(self, x, y, s1, s2):
        t = [[-1 for _ in range(y + 1)] for _ in range(x + 1)]

        for i in range(x + 1):
            t[i][0] = 0
        for i in range(y + 1):
            t[0][i] = 0

        for X in range(1, x + 1):
            for Y in range(1, y + 1):
                if s1[X - 1] == s2[Y - 1]:
                    t[X][Y] = 1 + t[X - 1][Y - 1]
                else:
                    t[X][Y] = max(t[X][Y - 1], t[X - 1][Y])

        return t

    def print_lcs(self, s1, s2, x, y):
        t = self.lcs(x, y, s1, s2)
        i, j = x, y

        ans = ''
        while i > 0 and j > 0:
            if s1[i - 1] == s2[j - 1]:
                ans = ans + s1[i - 1]
                i, j = i - 1, j - 1
            else:
                if t[i][j - 1] > t[i - 1][j]:
                    j = j - 1
                else:
                    i = i - 1
        return ans[::-1]

    def LCSof3(self, A, B, C, n1, n2, n3):
        # code here
        s1 = self.print_lcs(A, B, n1, n2)
        print(s1)
        x = len(s1)
        return self.lcs_sol(x, n3, s1, C)


if __name__ == '__main__':
    s1 = 'ffmznimkkas'
    s2 = 'vwsrenzkycx'
    s3 = 'fxtlsgy'
    x, y, z = len(s1), len(s2), len(s3)
    a = Solution()
    print(a.LCSof3(s1, s2, s3, x, y, z))

