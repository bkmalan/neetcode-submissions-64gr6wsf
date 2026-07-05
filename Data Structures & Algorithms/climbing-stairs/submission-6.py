class Solution:
    def climbStairs(self, n: int) -> int:

        cache = [-1] * (n + 1) 

        def dp(n):
            if n == 0:
                return 1
            if n < 0:
                return 0

            if cache[n] is not -1:
                return cache[n]

            cache[n] = dp(n - 1) + dp(n - 2)
            return cache[n]
        
        return dp(n)