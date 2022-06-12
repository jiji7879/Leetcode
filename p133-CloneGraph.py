"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        nodedict = {}
        nodelist = [node]
        while(nodelist != []):
            firstnode = nodelist.pop(0)
            if firstnode.val not in nodedict:
                neighborlist = []
                for i in firstnode.neighbors:
                    neighborlist.append(i.val)
                    nodelist.append(i)
                nodedict[firstnode.val] = neighborlist

        print(nodedict)
        clonedict = {}
        for item in nodedict:
            clonedict[item] = Node(item)
        for item in clonedict:
            for neighbor in nodedict[item]:
                clonedict[item].neighbors.append(clonedict[neighbor])
        return clonedict[1]    
