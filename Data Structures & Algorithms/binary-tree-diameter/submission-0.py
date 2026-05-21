# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def dfs(node):
            nonlocal longest
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)

            longest = max(longest, 2 + left + right)

            return 1 + max(left, right)



        dfs(root)
        return longest