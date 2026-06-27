class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        counter = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            counter[num] += 1
        
        for num, cnt in counter.items():
            freq[cnt].append(num)

        for i in range(len(freq) - 1, 0, -1):
            if len(res) == k:
                break
            if freq[i]:
                res.extend(freq[i])

        return res



        
            