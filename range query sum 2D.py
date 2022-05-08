class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            sums = 0
            for j in range(n):
                sums += matrix[i][j]
                matrix[i][j] = sums
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2 + 1):
            x1 = self.matrix[i][col2]
            x2 = 0 if col1 == 0 else self.matrix[i][col1 - 1]
            ans += x1 - x2
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
