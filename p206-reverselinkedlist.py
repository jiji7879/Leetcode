# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""version1
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        return self.reverseHelper(head.next, ListNode(head.val))

    def reverseHelper(self, curhead: Optional[ListNode], currev: Optional[ListNode]):
        if curhead == None:
            return currev
        a = ListNode(curhead.val)
        a.next = currev
        return self.reverseHelper(curhead.next, a)
"""
#version2
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        currev = ListNode(head.val)
        while head.next != None:
            head = head.next
            a = ListNode(head.val)
            a.next = currev
            currev = a
        return currev
