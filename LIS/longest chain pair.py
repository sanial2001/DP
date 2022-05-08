class Solution:
    def findLongestChain(self, pairs) -> int:
        n = len(pairs)
        t = [1 for _ in range(n)]
        pairs.sort(key=lambda x : x[0])

        for i in range(1, n):
            j = i-1
            temp = []
            while j >= 0:
                if pairs[i][0] > pairs[j][1]:
                    temp.append(t[j])
                j = j-1
            if len(temp) == 0:
                t[i] = 1
            else:
                t[i] = max(temp) + 1

        print(t)


if __name__ == '__main__':
    nums = [[1, 2], [7, 8], [4, 5]]
    Solution().findLongestChain(nums)
