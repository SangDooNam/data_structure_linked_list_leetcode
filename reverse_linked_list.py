# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        
        def reverse(node, prev=None):
            if not node:
                return prev
            
            next_node = node.next
            node.next = prev
            return reverse(next_node, node)
        
        return reverse(head)
        

# def reverse(head):
    
#     current = head
#     prev = None
    
#     while current:
#         next_node = current.next
#         current.next = prev
#         prev = current
#         current = next_node
#     return prev
    



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

head = [1,2,3,4,5]
head = create_linked_list(head)
sol = Solution()
reserved = sol.reverseList(head)
print_linked_list(reserved)
