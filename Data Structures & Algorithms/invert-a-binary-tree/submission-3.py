# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque()
        queue.append(root)

        while queue:
            for i in range(len(queue)):

                curr = queue.popleft()

                curr.right, curr.left = curr.left, curr.right

                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)


        return root