"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # base cases
        if not node:
            return node

        clone = {}
        # dfs
        def explore(node):
            # check
            if node in clone:
                return clone[node]
            # create
            newNode = Node(node.val)
            # cache
            clone[node] = newNode

            # connect
            for neighbor in node.neighbors:
                newNode.neighbors.append(explore(neighbor))
            
            return newNode


        return explore(node)