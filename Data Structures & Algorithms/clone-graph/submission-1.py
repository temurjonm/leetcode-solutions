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
            copy = Node(node.val)
            # cache
            clone[node] = copy
            # connect and explore neighboars
            for neighbor in node.neighbors:
                copy.neighbors.append(explore(neighbor))

            return copy

        return explore(node)