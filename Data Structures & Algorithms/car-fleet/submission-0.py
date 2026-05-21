class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]

        stack = []

        for p, s in sorted(pairs)[::-1]:
            time = (target - p)/s
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)

#    (pos, speed)
#  3        3      4.5.    10    
# (7, 1), (4, 2), (1, 2), (0,1) 
