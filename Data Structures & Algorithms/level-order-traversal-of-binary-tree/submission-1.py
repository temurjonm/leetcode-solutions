# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # solution 1 DFS
        # store result in list
        # traverse - level by level starting from root, pass level number, store level in hashtable
        # second pass traverse hash table and add to list
        '''
            {
                0: [1],
                1: [2]
            }
        '''
        # base case
        if not root:
            return []

        result = []
        mapping = defaultdict(list)

        def levels(node, level):
            if not node:
                return 

            mapping[level].append(node.val)

            if node.left:
                levels(node.left, level+1)
            if node.right:
                levels(node.right, level+1)

        levels(root, 0)

        for key in sorted(mapping):
            result.append(mapping[key])

        return result



            
