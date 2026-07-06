class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        curLen = 1
        maxLen = 0
        
        sortedNums = sorted(nums)

        for i in range(1, len(sortedNums)):
            if sortedNums[i - 1] == sortedNums[i]:
                continue
            if (sortedNums[i - 1] + 1) == sortedNums[i]:
                curLen += 1
            else:
                maxLen = max(maxLen, curLen)
                curLen = 1
        
        return max(maxLen, curLen)


        