class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for str in strs:
            key = ''.join(sorted(str))
            map[key].append(str)
        
        return [ group for group in map.values()]