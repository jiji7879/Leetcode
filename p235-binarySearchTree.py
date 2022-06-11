# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""version 1
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = self.commonHelper(root, p, q)
        return result[2]

    def commonHelper(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> List[int]:
        commonleft = [0, 0, 0]
        commonright = [0, 0, 0]
        if root.left is not None:
            commonleft = self.commonHelper(root.left, p, q)
            if commonleft[0]==1 and commonleft[1]==1:
                return commonleft
        if root.right is not None:
            commonright = self.commonHelper(root.right, p, q)
            if commonright[0]==1 and commonright[1]==1:
                return commonright
        commonleft[0] = commonleft[0]+commonright[0]
        commonleft[1] = commonleft[1]+commonright[1]
        commonleft[2] = commonleft[2]+commonright[2]
        if root.val == p.val:
            commonleft[0] = 1
        elif root.val == q.val:
            commonleft[1] = 1
        if commonleft[0]==1 and commonleft[1]==1:
            commonleft[2] = root
        return commonleft
"""
#version 2
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
