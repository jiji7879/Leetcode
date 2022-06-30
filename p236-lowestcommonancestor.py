# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""version 1
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        answerkey = self.ancestorhelper(root, p, q)
        return answerkey[2]
    def ancestorhelper(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> List[int]:
        answerleft = self.ancestorhelper(root.left, p, q) if root.left != None else [0,0,None]
        if answerleft[0]==1 and answerleft[1]==1:
            return answerleft
        answerright = self.ancestorhelper(root.right, p, q) if root.right != None else [0,0,None]
        if answerright[0]==1 and answerright[1]==1:
            return answerright
        answerkey = []
        answerkey.append(answerleft[0]+answerright[0])
        answerkey.append(answerleft[1]+answerright[1])
        if root.val == p.val:
            answerkey[0] = 1
        elif root.val == q.val:
            answerkey[1] = 1
        if answerkey[0]==1 and answerkey[1]==1:
            answerkey.append(root)
        else:
            answerkey.append(None)
        return answerkey
"""
#version 2
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q:
            return root
        answerkey = self.ancestorhelper(root, p, q)
        return answerkey[2]
    def ancestorhelper(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> List[int]:
        answerleft = self.ancestorhelper(root.left, p, q) if root.left != None else [0,0,None]
        if answerleft[0]==1 and answerleft[1]==1:
            return answerleft
        answerright = self.ancestorhelper(root.right, p, q) if root.right != None else [0,0,None]
        if answerright[0]==1 and answerright[1]==1:
            return answerright
        answerkey = []
        answerkey.append(answerleft[0]+answerright[0])
        answerkey.append(answerleft[1]+answerright[1])
        if root == p:
            answerkey[0] = 1
        elif root == q:
            answerkey[1] = 1
        if answerkey[0]==1 and answerkey[1]==1:
            answerkey.append(root)
        else:
            answerkey.append(None)
        return answerkey
