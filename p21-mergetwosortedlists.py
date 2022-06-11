# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = ListNode()
        b = a
        while list1!= None or list2!=None:
            if list1 == None:
                while list2!=None:
                    a.next = ListNode(list2.val)
                    list2 = list2.next
                    a = a.next
                break
            if list2 == None:
                while list1!=None:
                    a.next = ListNode(list1.val)
                    list1 = list1.next
                    a = a.next
                break
            if list1.val < list2.val:
                a.next = ListNode(list1.val)
                list1 = list1.next
                a = a.next
            else:
                a.next = ListNode(list2.val)
                list2 = list2.next
                a = a.next
        return b.next
