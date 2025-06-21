# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        depth = 0
        depth_ = defaultdict(list)
        result = []
        queue = [(root,0)]

        if not root:
            return result

        while queue:
            node, depth = queue.pop(0)
            depth_[depth].append(node.val)
    
            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        
        for i in range(depth+1):
            result.append(depth_[i][-1])

        return result


        
