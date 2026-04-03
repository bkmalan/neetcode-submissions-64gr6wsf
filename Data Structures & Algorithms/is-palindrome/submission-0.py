class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = s.replace(" ","").lower()
        str_len = len(stripped)
        i = 0
        j = str_len - 1 
        while i < j:
            c1 = stripped[i]
            c2 = stripped[j]
            if not c1.isalnum():
                i += 1
                continue
            if not c2.isalnum(): 
                j -= 1
                continue
            if c1 != c2:
                return False
            i += 1
            j -= 1
        return True
        
