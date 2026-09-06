# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()

        nested = []

        if root:
            queue.append(root)

        while len(queue) > 0:
            level = []
            for i in range(len(queue)): #runs as many times as there are nodes in that level 
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            #level.append(queue)
            nested.append(level)
        return nested


