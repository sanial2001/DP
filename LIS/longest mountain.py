class Solution:
    def longestMountain(self, arr) -> int:
        n = len(arr)
        i = 1
        ans = 0
        while i < n-1:
            j = i-1
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                cnt = 1
                while j > 0 and arr[j] > arr[j-1]:
                    cnt += 1
                    j -= 1
                j = i
                while j < n-1 and arr[j+1] > arr[j]:
                    cnt += 1
                    j += 1
                i = j
                ans = max(ans, cnt)
            else:
                i += 1
        print(ans)


if __name__ == '__main__':
    arr = [2,1,4,7,3,2,5]
    Solution().longestMountain(arr)