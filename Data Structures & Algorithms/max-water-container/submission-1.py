class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        most = 0

        while left < right:
            candidate = min(heights[left], heights[right]) * (right - left)

            most = max(most, candidate)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return most

# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
#         left, right = 0, len(heights) - 1
        
#         most = 0
#         while (left < right):
#             candidate = (right - left) * min(heights[left], heights[right])
#             most = max(most, candidate)

#             if left < right:
#                 left += 1
#             else:
#                 right -= 1
        
#         return most
