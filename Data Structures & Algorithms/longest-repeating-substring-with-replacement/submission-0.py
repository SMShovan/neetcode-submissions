class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        longestRep = 0
        left = 0
        right = 0
        
        maxFreq = 0
        for i, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            
            maxFreq = max(count[c], maxFreq)


            while (i - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            
            longestRep = max(longestRep, i - left + 1)

        return longestRep



# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         count = {}

#         res = 0

#         l = 0

#         maxf = 0

#         for r in range(len(s)):
#             count[s[r]] = 1 + count.get(s[r], 0)
#             maxf = max(maxf, count[s[r]])

#             while (r - l + 1) - maxf > k:
#                 count[s[l]] -= 1
#                 l += 1
            
#             res = max(res, r - l + 1)
        
#         return res