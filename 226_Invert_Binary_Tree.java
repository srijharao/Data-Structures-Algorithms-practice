class Solution {
    public TreeNode invertTree(TreeNode root) {

        if(root == null){
            return root;
        }

        TreeNode left = root.left;
        TreeNode right = root.right;

        root.right = left;
        root.left = right;

        invertTree(root.left);
        invertTree(root.right); 
        
        return root;
        
    }
}
