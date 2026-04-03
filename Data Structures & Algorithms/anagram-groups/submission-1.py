class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            mapper[key].append(s)

        return list(mapper.values())