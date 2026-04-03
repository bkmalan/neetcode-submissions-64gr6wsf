class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for n in nums:
            res[n] += 1
        frequencies = sorted(res.values())
        lowestK = frequencies[max(0, len(frequencies) - k)]
        return [key for key, v in res.items() if v >= lowestK]
