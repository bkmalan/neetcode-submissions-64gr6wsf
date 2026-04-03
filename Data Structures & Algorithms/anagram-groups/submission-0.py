class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        grouped = {}
        for s in strs:
            factorial = 1
            for c in s:
                factorial *= ord(c)
            key = f"{factorial}|{len(s)}" 
            if key in grouped:
                grouped[key].append(s)
            else:
                grouped[key] = [s]
        
        return list(grouped.values())