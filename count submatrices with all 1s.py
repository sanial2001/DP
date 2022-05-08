class Solution:
    def numSubmat(self, mat) -> int:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(1, n):
                if mat[i][j] == 1:
                    mat[i][j] = mat[i][j - 1] + 1
        res = 0
        for i in range(m):
            for j in range(n):
                temp = 1000000
                for k in range(i, m):
                    temp = min(temp, mat[k][j])
                    res += temp
        return res
