# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # keep track of max path so far
        # every node except child node should have max(left path, right path)
        # if a node has only left path, calculate left path, and compare to maxsofar
        # same with right
        self.maxpath_so_far = 0
        if not root:
            return 0

        def dfs(node):
            if node.left and node.right:
                left_path = dfs(node.left) + 1
                right_path = dfs(node.right) + 1
                self.maxpath_so_far = max(self.maxpath_so_far, left_path + right_path)
                return max(left_path,right_path) 
            elif node.left:
                left_path = dfs(node.left) + 1
                self.maxpath_so_far = max(self.maxpath_so_far, left_path)
                return left_path
                
            elif node.right:
                right_path = dfs(node.right) + 1
                self.maxpath_so_far = max(self.maxpath_so_far, right_path)
                return right_path
                
            else:
                return 0

        
        dfs(root)
        return self.maxpath_so_far
        
        
