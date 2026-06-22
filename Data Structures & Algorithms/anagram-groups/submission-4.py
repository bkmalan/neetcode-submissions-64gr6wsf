class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        grouped = defaultdict(list)

        for s in strs:
            counter = [0] * 26 # for lowercase letters
            for c in s:
                counter[ord(c) - ord('a')] += 1
            grouped[tuple(counter)].append(s)
        

        for group in grouped.values():
            res.append(group)
        
        return res