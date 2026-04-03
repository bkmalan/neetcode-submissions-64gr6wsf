class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter1 = {}
        counter2 = {}

        for i in range(len(s)):
            counter1[s[i]] = counter1.get(s[i], 0) + 1
            counter2[t[i]] = counter2.get(t[i], 0) + 1
        
        return counter1 == counter2