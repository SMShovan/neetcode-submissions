class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)

        longest = 0
        for num in nums:
            if num - 1 not in check:
                streak = 1
                next = num + 1
                while next in check:
                    streak +=1
                    next += 1
                longest = max(streak, longest)
        
        return longest