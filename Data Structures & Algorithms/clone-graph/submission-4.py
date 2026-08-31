class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        copy = {}

        def explore(node):
            # check
            if node in copy:
                return copy[node]

            # create 
            newNode = Node(node.val)

            copy[node] = newNode

            for neighboar in node.neighbors:
                newNode.neighbors.append(explore(neighboar))
            
            return newNode

        return explore(node)