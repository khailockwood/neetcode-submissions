# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left = self.height(root.left)
        right = self.height(root.right)
        print("left height" + str(left))
        print("right height" + str(right))
        if abs(left-right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, curr: Optional[TreeNode]):
        if not curr:
            return 0
        return 1 + max(self.height(curr.left), self.height(curr.right))