# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        levels = []

        while queue:
            nested = []
            for i in range(len(queue)):
                curr = queue.popleft()
                nested.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                    #ested.append(curr.left.val)

                if curr.right:
                    queue.append(curr.right)
                    #nested.append(curr.right.val)

            levels.append(nested)
        
        return (levels)
