# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [(root, 0)]
        dict_ = defaultdict(list)
        result = []

        if not root:
            return result
        
        while queue:
            node, col = queue.pop(0)

            if node.left:
                queue.append([node.left, col-1])
            if node.right:
                queue.append([node.right, col+1])
            
            dict_[col].append(node.val)

        min_col = min(dict_.keys())
        max_col = max(dict_.keys())

        while min_col <= max_col:
            result.append(dict_[min_col])
            min_col += 1
        
        return result
        
