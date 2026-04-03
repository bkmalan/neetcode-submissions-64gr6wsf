class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      Dict = {}
      for num in nums:
        print(Dict)
        if Dict.get(num,False):
            return True
        Dict[num] = True

      return False