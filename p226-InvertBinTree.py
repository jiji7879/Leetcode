# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""version 1
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        a = TreeNode(root.val)
        if root.right != None:
            a.left = self.invertTree(root.right)
        if root.left != None:
            a.right = self.invertTree(root.left)
        return a
"""
#version 2
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
