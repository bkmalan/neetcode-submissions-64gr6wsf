class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique = set(nums)
        maxLen = 0

        for num in unique:
            if num - 1 not in unique:
                curLen = 1
                curr = num
                while curr + 1 in unique:
                    curLen += 1
                    curr += 1
                maxLen = max(curLen, maxLen)

        

        return maxLen


