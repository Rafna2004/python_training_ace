from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def hasCycle(head: Optional[ListNode]) -> bool:
    """
    Determines if the linked list has a cycle in it using Floyd's Cycle-Finding Algorithm
    (Slow and Fast Pointers / Tortoise and Hare).

    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return False
        
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
            
    return False

# Helper function to create a linked list with a cycle for testing
def create_linked_list_with_cycle(values: list, pos: int) -> Optional[ListNode]:
    if not values:
        return None
    
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
        
    if pos != -1 and 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]
        
    return nodes[0]

if __name__ == "__main__":
    # Test Case 1: head = [3,2,0,-4], pos = 1 -> True
    head1 = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    print("Test Case 1 (Cycle at index 1):", hasCycle(head1))  # Expected: True

    # Test Case 2: head = [1,2], pos = 0 -> True
    head2 = create_linked_list_with_cycle([1, 2], 0)
    print("Test Case 2 (Cycle at index 0):", hasCycle(head2))  # Expected: True

    # Test Case 3: head = [1], pos = -1 -> False
    head3 = create_linked_list_with_cycle([1], -1)
    print("Test Case 3 (No cycle):", hasCycle(head3))          # Expected: False

    # Test Case 4: Empty List -> False
    head4 = create_linked_list_with_cycle([], -1)
    print("Test Case 4 (Empty list):", hasCycle(head4))        # Expected: False
