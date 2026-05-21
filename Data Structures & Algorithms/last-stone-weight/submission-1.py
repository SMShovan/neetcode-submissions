class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesheap = [-s for s in stones]
        heapq.heapify(stonesheap)

        while len(stonesheap) > 1:
            stone1 = heapq.heappop(stonesheap)
            stone2 = heapq.heappop(stonesheap)
            
            newStone = stone1 - stone2
            if stone1 < stone2:
                heapq.heappush(stonesheap, newStone) 
        stonesheap.append(0)
        return stonesheap[0] * -1
