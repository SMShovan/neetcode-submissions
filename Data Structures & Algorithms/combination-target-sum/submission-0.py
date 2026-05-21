class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        current = []
        def dfs(index, total):
            if total == target:
                res.append(current.copy())
                return
            if index >= len(nums) or total > target:
                return 
            
            current.append(nums[index])
            dfs(index, total + nums[index])
            current.pop()
            dfs(index + 1, total)

        dfs(0, 0)
        return res

