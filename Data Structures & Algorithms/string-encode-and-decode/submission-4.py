class Solution:
    def encode(self, strs: List(str)) ->str:
        res = ''
        
        for s in strs:
            res += str(len(s)) + "$" + s
        return res
    
    def decode(self, s: str) -> List[str]:
        strs = []

        i = 0
        
        while i < len(s):
            j = i

            while s[i] != "$":
                i += 1
            
            length = int(s[j:i])
            strs.append(s[i + 1 : i + 1 + length])

            j = i + 1 + length
            i = j
        return strs


# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         res = ''
#         for s in strs:
#             res += str(len(s)) + "$" + s
        
#         return res

#     def decode(self, s: str) -> List[str]:
#         strs = []
#         i = 0

#         while (i < len(s)):
#             j = i
#             while (s[j] != "$"):
#                 j = j + 1
            
#             length = int(s[i:j])
#             strs.append( s[j + 1 : j + 1 + length])

#             i = j + 1 + length


#         return strs