class Solution:
        def __init__(self):
            self.dx = [1, 2, 2, 1, -1, -2, -2, -1]
            self.dy = [2, 1, -1, -2, -2, -1, 1, 2]

        def inside(self, x, y, N):
            return (x >= 0 and x < N and y >= 0 and y < N)

        def findProb(self, N, start_x, start_y, steps):

            # Code here
            # dp array
            dp1 = [[[0 for i in range(N + 5)] for j in range(N + 5)] for k in range(steps + 5)]

            # For 0 number of steps, each
            # position will have probability 1
            for i in range(N):
                for j in range(N):
                    dp1[i][j][0] = 1

            # for every number of steps s
            for s in range(1, steps + 1):

                # for every position (x,y) after
                # s number of steps
                for x in range(N):

                    for y in range(N):
                        prob = 0.0

                        # For every position reachable from (x,y)
                        for i in range(N):
                            nx = x + self.dx[i]
                            ny = y + self.dy[i]

                            # if this position lie inside the board
                            if (self.inside(nx, ny, N)):
                                prob += dp1[nx][ny][s - 1] / 8.0

                        # store the result
                        dp1[x][y][s] = prob

            # return the result
            return dp1[start_x][start_y][steps]