class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        maxLen = 0
        for num in unique:
            if not num - 1 in unique:
                curLen = 1
                nextNum = num + 1
                while nextNum in unique:
                    curLen += 1
                    nextNum += 1
                maxLen = max(curLen, maxLen)
        
        return maxLen