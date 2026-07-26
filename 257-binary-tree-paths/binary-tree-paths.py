# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        def dfs(node,path):
            if node is None:
                return
            if node.left is None and node.right is None:
                ans.append(path)
                return
            if node.left:
                dfs(node.left,path+"->"+str(node.left.val))
            if node.right:
                dfs(node.right, path + "->" + str(node.right.val))
        if root:
            dfs(root, str(root.val))

        return ans


        