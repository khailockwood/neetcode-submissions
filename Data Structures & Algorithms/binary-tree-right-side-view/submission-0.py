# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #need to search right to left at each level
        #as soon as we hit a non null node, add to the list
        queue = deque()

        rights = []

        if root:
            queue.append(root)

        while len(queue) > 0:

            for i in range(len(queue)):
                curr = queue.popleft()
                if i == 0:
                    rights.append(curr.val)
                print("Rights: " + str(rights))
                if curr.right:
                    queue.append(curr.right)
                    #rights.append(curr.right.val)
                if curr.left:
                    queue.append(curr.left)
                    #rights.append(curr.left.val)
        return rights