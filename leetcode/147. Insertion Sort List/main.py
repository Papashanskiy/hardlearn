# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = head
        l = [head]
        curr = head.next
        index = 1
        while curr:
            l.append(curr)
            current_index = index
            while current_index > 0 and l[current_index-1].val > l[current_index].val:
                l[current_index].val, l[current_index -
                                        1].val = l[current_index-1].val, l[current_index].val
                current_index -= 1
            curr = curr.next
            index += 1

        return result
