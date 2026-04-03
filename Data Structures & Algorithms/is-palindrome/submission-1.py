class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_len = len(s)
        i = 0
        j = str_len - 1 
        while i < j:
            c1 = s[i]
            c2 = s[j]
            if not c1.isalnum():
                i += 1
                continue
            if not c2.isalnum(): 
                j -= 1
                continue
            if c1.lower() != c2.lower():
                return False
            i += 1
            j -= 1
        return True
        
