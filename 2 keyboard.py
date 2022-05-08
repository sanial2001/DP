class Solution:
    def minSteps(self, n: int) -> int:
        t = [0 for _ in range(n+1)]
        t[0], t[1], t[2] = 0, 1, 2

        for i in range(3, n+1):
            j = 2
            temp = 0
            while j < i:
                if i % j == 0:
                    temp = t[j] + t[i//j]
                    break
                j = j+1
            if j == i:
                t[i] = i
            else:
                t[i] = temp

        print(t)


if __name__ == '__main__':
    Solution().minSteps(18)
