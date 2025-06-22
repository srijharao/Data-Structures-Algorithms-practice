# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        result = []
        def dfs(node, pathnum):
            if node.left:
                dfs(node.left, (pathnum * 10) + node.left.val)
            if node.right:
                dfs(node.right, (pathnum * 10) + node.right.val)
            if node.left is None and node.right is None:
                result.append(pathnum)


        dfs(root, root.val)

        return sum(result)
