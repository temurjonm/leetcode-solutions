# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        totalMax = 0
        if not root: return 0

        queue = deque([(root, root.val)])

        while queue:
            node, maxVal = queue.popleft()

            if node.val >= maxVal:
                totalMax += 1

            if node.left:
                queue.append((node.left, max(node.val, maxVal)))

            if node.right:
                queue.append((node.right, max(node.val, maxVal)))

        return totalMax