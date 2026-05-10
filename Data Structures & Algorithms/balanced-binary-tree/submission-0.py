# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def balance(node):
            if not node: return 0
            left, right = balance(node.left), balance(node.right)
            return max(left, right) + 1

        left = balance(root.left)
        right = balance(root.right)

        if abs(left - right) > 1: return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)