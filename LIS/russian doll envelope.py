class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        envelopes.sort(key= lambda x : x[0])
        print(envelopes)
        n = len(envelopes)
        t = [1 for _ in range(n)]

        for i in range(1, n):
            j = i-1
            temp = []
            while j >= 0:
                if envelopes[i][1] > envelopes[j][1] and envelopes[i][0] > envelopes[j][0]:
                    temp.append(t[j])
                j = j-1
            if len(temp) > 0:
                t[i] = max(temp) + 1

        print(max(t))


if __name__ == '__main__':
    en = [[4,5],[4,6],[6,7],[2,3],[1,1]]
    Solution().maxEnvelopes(en)
