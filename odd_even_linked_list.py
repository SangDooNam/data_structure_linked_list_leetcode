# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        if not head or not head.next or not head.next.next:
            return head
        
        odd = head
        even = head.next
        even_head = even
        
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
            
        odd.next = even_head
        
        return head

def create_linked_list(values):
    
    head =  ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    
    return head

def print_linked_list(head):
    current = head
    
    while current:
        print(current.val, end=' ')
        current = current.next
    
    print()
    
    
# head = [2,1,3,5,6,4,7]
head = create_linked_list([2,1,3,5,6,4,7])

sol = Solution()
sol.oddEvenList(head)
print_linked_list(head)

