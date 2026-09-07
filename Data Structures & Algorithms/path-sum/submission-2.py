# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum = targetSum - root.val #subtract .val every time we dfs, if end of path == 0 then we have a sum
        if targetSum == 0 and not root.left and not root.right: #has to be a leaf node, and path has to equal targetSum
            return True
        if self.hasPathSum(root.left, targetSum):
            return True
        if self.hasPathSum(root.right, targetSum):
            return True

        return False
