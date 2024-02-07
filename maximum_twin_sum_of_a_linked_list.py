# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head):
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, current = None, slow
        
        while current:
            next_node = current.next
            current.next = prev
            prev =  current
            current = next_node
        
        second_half_node = prev
        first_half_node = head
        maximum_sum = 0
        while second_half_node:
            twin_sum = first_half_node.val + second_half_node.val
            maximum_sum = max(maximum_sum, twin_sum)
            first_half_node = first_half_node.next
            second_half_node = second_half_node.next
        
        return maximum_sum


def create_linked_list(values):
    
    head = ListNode(values[0])
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

sol = Solution()
# head = create_linked_list([4,2,2,3])
head = create_linked_list([5,4,2,1])

print(sol.pairSum(head))