# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS approach
        if not root:
            return []

        queue = deque([(root, 0)])
        mapping = defaultdict(list)
        min_value = max_value = 0

        while queue:
            node, level = queue.popleft()
            min_value = min(min_value, level)
            max_value = max(max_value, level)

            mapping[level].append(node.val)
            if node.left:
                queue.append([node.left, level + 1])

            if node.right:
                queue.append([node.right, level + 1])

        result = []
        for i in range(min_value, max_value+1):
            result.append(mapping[i])

        return result