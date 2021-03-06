#定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
###################################solution 1##############################################
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if cur is None:
                return pre
            res = recur(cur.next, cur)
            cur.next = pre
            return res
        return recur(head, None)
    
###################################solution 2##############################################
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur:
            res = cur.next
            cur.next = pre
            pre = cur
            cur = res
        return pre
