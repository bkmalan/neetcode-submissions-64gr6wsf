class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                diff = nums[i] + nums[start] + nums[end]
                triplet = [nums[i], nums[start], nums[end]]
                if diff == 0:
                    if triplet not in res:
                        res.append([nums[i], nums[start], nums[end]])
                    start += 1
                elif diff < 0:
                    start += 1
                else:
                    end -= 1
        return res