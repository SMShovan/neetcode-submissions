class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        res = []

        #2 3 4
        #1 2 6 (pre)
        #12 4 1 (post)
        for i in range(1, len(nums), 1):
            
            pre[i] = pre[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
           
            post[i] = post[i + 1] * nums[i + 1]

        for i in range(0, len(nums), 1):
            
            res.append(pre[i] * post[i])
        
        return res
        
