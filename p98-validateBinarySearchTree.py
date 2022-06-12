# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return None
        checklist = [[root, -inf, inf]]
        while checklist != []:
            a = checklist.pop(0)
            if a[0].left != None:
                if a[0].left.val >= a[0].val or a[0].left.val <= a[1]:
                    return False
                checklist.append([a[0].left, a[1], a[0].val])
            if a[0].right != None:
                if a[0].right.val <= a[0].val or a[0].right.val >= a[2]:
                    return False
                checklist.append([a[0].right, a[0].val, a[2]])
        return True
