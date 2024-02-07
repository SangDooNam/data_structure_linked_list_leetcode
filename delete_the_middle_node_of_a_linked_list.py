# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None

        # Calculate the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Find the node before the middle node
        middle_index = length // 2
        current = head
        for _ in range(middle_index - 1):
            current = current.next

        # Delete the middle node
        current.next = current.next.next

        return head



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
    

head = create_linked_list([1,3,4,7,1,2,6])
sol = Solution()
sol.deleteMiddle(head)
print_linked_list(head)


