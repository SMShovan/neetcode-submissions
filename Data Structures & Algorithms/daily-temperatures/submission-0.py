class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for day, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                removed = stack.pop()
                res[removed[0]] = day - removed[0]
            stack.append((day, temperature))

        return res