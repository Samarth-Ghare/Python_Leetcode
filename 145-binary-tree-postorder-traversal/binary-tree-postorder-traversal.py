# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, TeriMaaKiChut):
        chalbe = []
        def bsdk(TeriMaaKiChut):
            if not TeriMaaKiChut:
                return

            bsdk(TeriMaaKiChut.left)
            bsdk(TeriMaaKiChut.right)
            chalbe.append(TeriMaaKiChut.val)

        bsdk(TeriMaaKiChut)
        return chalbe