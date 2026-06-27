class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l, r = 0, len(nums) - 1


        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res.append(pow(nums[l], 2))
                l += 1
            else:
                res.append(pow(nums[r], 2))
                r -= 1
        

        return res[::-1]


