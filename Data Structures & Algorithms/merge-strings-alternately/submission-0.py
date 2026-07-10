class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''

        l, r = 0, 0

        while l < len(word1) and r < len(word2):
            merged += word1[l]
            l += 1
            merged += word2[r]
            r += 1
        
        merged += word1[l:] if r == len(word2) else word2[r:]

        return merged



         