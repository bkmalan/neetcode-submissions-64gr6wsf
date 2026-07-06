class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        maxLen = 0

        for num in unique:
            if num - 1 not in unique:
                seqLen = 1
                while num + seqLen in unique: # adding total seqlen or doing +1 each time is the same
                    seqLen += 1
                maxLen = max(seqLen, maxLen)

        return maxLen


