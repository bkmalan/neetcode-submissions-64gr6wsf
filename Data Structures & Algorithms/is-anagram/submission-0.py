class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = {}
        for char in s:
            if counter.get(char,False):
                counter[char] = counter[char]+1
            else:
                counter[char] = 1
        for char in t:
            if counter.get(char,False):
                counter[char] = counter[char]-1
                if counter[char]==0:
                    del counter[char]
            else:
                return False
        return not counter
                


        