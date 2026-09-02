class Solution:
    def climbStairs(self, n: int) -> int:
        d = [0] * n
        d[0] = 1
        if n == 1:
            return 1
        d[1] = 2
        print (d)
        for i in range(2,n):
            d[i] = d[i-1] + d[i-2]
            print(d[i])
        return d[n-1] 