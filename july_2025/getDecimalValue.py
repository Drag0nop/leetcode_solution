"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

Example:

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cnt = 0
        while head:
            cnt = cnt * 2 + head.val  # Shift left and add bit
            head = head.next
        return cnt

def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Example input
binary_digits = [1, 0, 1]  # Binary 101
head = create_linked_list(binary_digits)

# Run the solution
sol = Solution()
print(sol.getDecimalValue(head)) # Output: 5