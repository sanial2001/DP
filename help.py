class Solution:

    # Complete this function

    # Function to return the name of candidate that received maximum votes.
    def winner(self, arr, n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        d = {}
        for val in arr:
            d[val] = d.get(val, 0) + 1
        d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        print(d[0][0])


if __name__ == '__main__':
    Solution().winner(arr=['john', 'johnny', 'jackie', 'johnny', 'john', 'jackie', 'jamie',
                           'jamie', 'john', 'johnny', 'jamie', 'johnny', 'john'], n=13)
