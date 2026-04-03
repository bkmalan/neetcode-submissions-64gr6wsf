class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dict = {}
        for i in range(len(nums)):
            if Dict.get(target-nums[i],-1)>-1:
                return [Dict.get(target-nums[i]),i]
            Dict[nums[i]] = i