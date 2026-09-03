# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None #got to the bottom
        
        #search tree now:

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else: #root.val == key, we've found node we want to delete
            if not root.right: #if node we are deleting as only a left node, replace with left
                return root.left 
            elif not root.left:
                return root.right
            else: # has both children
                #find min value that is to the right of current node
                newNode = self.minValue(root.right)
                root.val = newNode.val
                root.right = self.deleteNode(root.right, newNode.val) #now that val in min node to the right has replaced deleted node, need to remove that node thats "moved up" and connect it's potential children
        return root
    def minValue(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

