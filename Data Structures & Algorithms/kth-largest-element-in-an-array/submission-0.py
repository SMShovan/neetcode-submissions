class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        k = len(nums) - k
        def quickselect(nums, left, right):
            pivot, p = nums[right], left

            for i in range(left, right):
                if (nums[i] <= pivot):
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[right] = nums[right], nums[p]

            if p > k:
                return quickselect(nums,left, p - 1)
            elif p < k:
                return quickselect(nums, p + 1, right)
            else:
                return nums[p]

        return quickselect(nums, 0, len(nums) - 1)