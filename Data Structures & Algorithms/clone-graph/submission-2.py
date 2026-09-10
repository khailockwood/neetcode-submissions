"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        oldToNew = {}
        queue = deque()

        oldToNew[node] = Node(node.val)
        queue.append(node)

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                for neighbor in curr.neighbors:

                    if neighbor not in oldToNew:
                        cloneNode = Node(neighbor.val)
                        oldToNew[neighbor] = cloneNode
                        queue.append(neighbor)

                    oldToNew[curr].neighbors.append(oldToNew[neighbor]) #oldToNew[curr] gives us the clone of the current node (with original mapped to current), then we add to the neighbors of that clone the clone of the neighbor we are looking at, as oldToNew[neighbor] = cloneNode           
        return oldToNew[node]




