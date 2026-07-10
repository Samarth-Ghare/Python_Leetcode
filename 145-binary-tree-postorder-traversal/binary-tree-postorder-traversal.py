# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        chalbe = []
        def bsdk(root):
            if not root:
                return

            bsdk(root.left)
            bsdk(root.right)
            chalbe.append(root.val)

        bsdk(root)
        return chalbe