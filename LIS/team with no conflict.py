


class Solution:
    def bestTeamScore(self, scores, ages) -> int:
        n = len(scores)
        team = []
        for i in range(n):
            team.append([ages[i], scores[i]])
        team.sort()
        print(team)
        t = [0 for _ in range(n)]
        t[0] = team[0][1]

        for i in range(1, n):
            j = i-1
            temp = []
            while j >= 0:
                if team[i][1] >= team[j][1]:
                    temp.append(t[j])
                j = j-1
            if len(temp) > 0:
                t[i] = max(temp) + team[i][1]
            else:
                t[i] = team[i][1]

        print(t)


if __name__ == '__main__':
    scores = [1, 3, 7, 3, 2, 4, 10, 7, 5]
    ages = [4, 5, 2, 1, 1, 2, 4, 1, 4]
    Solution().bestTeamScore(scores, ages)
