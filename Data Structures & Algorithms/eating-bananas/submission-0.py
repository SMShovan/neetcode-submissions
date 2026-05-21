class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)
        maximum = right
        while left <= right:
            mid = int((left + right)//2)
            hours = 0

            for pile in piles:
                hours += math.ceil((pile/ mid))

            if (hours <= h):
                maximum = min (maximum, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return maximum
