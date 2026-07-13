class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = nums[0]

        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] <= nums[right]:
                smallest = min(smallest, nums[left])
                break
            mid = (left + right) // 2
            smallest = min(smallest, nums[mid])
            if nums[mid] >= nums[left] :
                left = mid + 1
            else:
                right = mid - 1

        return smallest
        