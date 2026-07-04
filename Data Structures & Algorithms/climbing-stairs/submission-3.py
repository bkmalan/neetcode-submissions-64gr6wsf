class Solution:
    def climbStairs(self, n: int) -> int:

        mem = {}

        def dp(n):
            if n == 0:
                return 1
            if n < 0:
                return 0

            res1 = mem.get(f"{n}#1") if mem.get(f"{n}#1") is not None else dp(n - 1)
            res2 = mem.get(f"{n}#2") if mem.get(f"{n}#2") is not None else dp(n - 2)
            if f"{n}#1":
                mem[f"{n}#1"] = res1
            if not f"{n}#2":
                mem[f"{n}#2"] = res2
            return res1 + res2
        
        return dp(n)