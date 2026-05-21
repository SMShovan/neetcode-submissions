class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        list = []

        for key, val in map.items():
            list.append((val, key))
        
        heapq.heapify(list)

        while (len(list) > k):
            heapq.heappop(list)
        
        return [ key for (val, key) in list]

