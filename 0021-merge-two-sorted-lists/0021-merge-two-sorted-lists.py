# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list1, list2 값 중 작은 값이 왼쪽에 오게 함
        if (not list1) or (list2 and list1.val > list2.val): # or 보다 and가 우선순위가 높음!
            list1, list2 = list2, list1
        # 그 다음 값이 계속 엮이도록 재귀 호출
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)

        return list1
        