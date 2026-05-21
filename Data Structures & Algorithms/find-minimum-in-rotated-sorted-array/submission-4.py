class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minimum = max(nums) + 1
        while left <= right:
            mid = int((left + right) // 2)
            minimum = min(minimum, nums[mid])
            if nums[left] < nums[right]:
                minimum = min(minimum, nums[left])
                break
            if (nums[mid] >= nums[left]):
                left = mid + 1
            else:
                right = mid - 1

        return minimum