# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self, result = True):
        self.result = result

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        self.height(root)
        return self.result

    def height(self, root: Optional[TreeNode]) -> int:
        if root.left is not None:
            lheight = self.height(root.left)
        else:
            lheight = 0
        if root.right is not None:
            rheight = self.height(root.right)
        else:
            rheight = 0
        if lheight-rheight > 1 or rheight-lheight > 1:
            self.result = False
        return max(lheight, rheight)+1
