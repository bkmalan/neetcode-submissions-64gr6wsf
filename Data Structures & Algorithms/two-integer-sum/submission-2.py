class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for idx, num in enumerate(nums):
            if target - num in diff_map:
                return [diff_map[target - num], idx]
            diff_map[num] = idx
        
        return []