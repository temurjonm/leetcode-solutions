# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # base case 
        if not root:
            return []

        queue = deque([root])

        result = []

        while queue:
            levels = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                levels.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


            result.append(levels)

        return result
            