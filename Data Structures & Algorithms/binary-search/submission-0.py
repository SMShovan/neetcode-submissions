class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums) - 1

        left, right = 0, length

        while left <= right:
            mid = int((left + right)// 2)

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
            
        return -1

