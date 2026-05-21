# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum = float('-inf')

        def dfs(root):
            nonlocal maximum
            if not root:
                return 0
            leftmax = max(0, dfs(root.left))
            rightmax = max(0, dfs(root.right))

            maximum = max(maximum, root.val + leftmax + rightmax)
            return max(root.val + leftmax, root.val + rightmax)
            

        dfs(root)
        return maximum