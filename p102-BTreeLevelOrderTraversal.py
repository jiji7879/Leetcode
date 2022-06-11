# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return None
        traversallist = [root]
        traversalnextlevel = []
        levelordertraversal = [[root.val]]
        thing1 = []
        while len(traversallist)>0 or len(traversalnextlevel)>0:
            if len(traversallist)==0:
                levelordertraversal.append(thing1)
                thing1 = []
                traversallist = traversalnextlevel
                traversalnextlevel = []
            node = traversallist.pop(0)
            if node.left != None:
                traversalnextlevel.append(node.left)
                thing1.append(node.left.val)
            if node.right != None:
                traversalnextlevel.append(node.right)
                thing1.append(node.right.val)
        if thing1 != []:
            levelordertraversal.append(thing1)
        return levelordertraversal
