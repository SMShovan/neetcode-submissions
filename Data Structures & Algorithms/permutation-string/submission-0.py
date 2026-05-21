class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        maps1 = {}
        for c in s1:
            maps1[c] = maps1.get(c, 0) + 1
    
        
        for i in range( len(s2) - len(s1) + 1):
            maps2 = {}
            for j in range(len(s1)):
                c = s2[i + j]
                maps2[c] = maps2.get(c, 0) + 1
            
            if maps1 == maps2:
                return True
        
        return False