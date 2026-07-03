# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        hq = []
        for head in lists:
            curr = head
            count = 0
            while curr:
                heapq.heappush(hq, curr.val)
                curr = curr.next
                count += 1
        
        curr = dummy
        while hq:
            curr.next = ListNode(heapq.heappop(hq))
            curr = curr.next


        return dummy.next     