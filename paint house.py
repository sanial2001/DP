class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        m, n = len(A), 3
        t = [[-1 for _ in range(n)] for _ in range(m)]

        for i in range(n):
            t[0][i] = A[0][i]

        for i in range(1, m):
            t[i][0] = min(t[i - 1][1], t[i - 1][2]) + A[i][0]
            t[i][1] = min(t[i - 1][0], t[i - 1][2]) + A[i][1]
            t[i][2] = min(t[i - 1][0], t[i - 1][1]) + A[i][2]

        return min(t[m-1])


if __name__ == '__main__':
    m = [[1, 5, 7],
         [5, 8, 4],
         [3, 2, 9],
         [1, 2, 4]]
    print(Solution().solve(m))
