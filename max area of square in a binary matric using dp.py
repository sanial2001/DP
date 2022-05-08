class Solution:
    def maxSquare(self, n, m, mat):
        # code here
        t = [[-1 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    t[i][j] = 0

        for i in range(n):
            if t[i][m - 1] == -1:
                t[i][m - 1] = 1

        for i in range(m):
            if t[n - 1][i] == -1:
                t[n - 1][i] = 1

        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                if t[i][j] == -1:
                    t[i][j] = min(t[i + 1][j + 1], t[i][j + 1], t[i + 1][j]) + 1

        for val in t:
            print(val)

        max_val = -1000
        for val in t:
            max_val = max(max_val, max(val))

        return max_val


if __name__ == '__main__':
    mat = [[0, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 0],
           [0, 1, 1, 1, 1, 0],
           [0, 0, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1]]
    print(Solution().maxSquare(5, 6, mat))
