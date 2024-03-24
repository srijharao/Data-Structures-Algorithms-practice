class Solution:
    def depth(self, root, count) -> int:
         # returns count
        if(root is None):
            return count
        count = count + 1 
        return max(self.depth(root.left, count) , self.depth(root.right, count))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
      count = 1
        if(root is None):
            return 0
        return max(self.maxDepth(root.left, count), self.maxDepth(root.right, count))
