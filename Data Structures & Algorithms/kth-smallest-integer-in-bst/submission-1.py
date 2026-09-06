# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = []
        
        def inOrderTraversal(node):
            if not node or len(visited) == k:
                return
            inOrderTraversal(node.left)
            if len(visited) < k:
                visited.append(node.val)
                inOrderTraversal(node.right)
        inOrderTraversal(root)
        return visited[k-1]
