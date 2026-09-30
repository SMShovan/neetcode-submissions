class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}

        # if len(c) != len(t):
        #     return False

        for c in s:
            map[c] = map.get(c, 0) + 1
        
        for c in t:
            if c not in map or map.get(c) == 0:
                return False
            map[c] -= 1
        
        for val in map.values():
            if val > 0:
                return False
        
        return True

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         map = {}

#         for c in s:
#             map[c] = map.get(c, 0) + 1
        
#         for c in t:
#             if c not in map or map[c] == 0:
#                 return False
#             else:
#                 map[c] = map[c] - 1
        
#         for val in map.values():
#             if val > 0:
#                 return False
#         return True
            

