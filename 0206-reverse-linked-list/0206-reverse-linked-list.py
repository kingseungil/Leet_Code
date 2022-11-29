# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # 1. 재귀 구조
        # def reverse(node: ListNode, prev: ListNode = None):
        #     if not node:
        #         return prev
        #     # node.next에는 이전 prev 리스트를 계속 연결
        #     next, node.next = node.next, prev
        #     # 다음 노드 next와 현재 노드 node를 파라미터로 지정한 함수를 계속해서 재귀 호출
        #     return reverse(next, node)
        # return reverse(head)
    
        # 2. 반복 구조
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
        
