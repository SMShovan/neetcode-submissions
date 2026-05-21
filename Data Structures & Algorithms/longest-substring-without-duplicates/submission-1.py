class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        left, right = 0, 0
        map = {}
        
        while right < len(s):
            map[s[right]] = map.get(s[right], 0) + 1
            if map[s[right]] == 2:
                while s[left] != s[right]:
                    map[s[left]] -=1
                    left += 1
                    
                map[s[right]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
            right += 1
        
        return longest

            