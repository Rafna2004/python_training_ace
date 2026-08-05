from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merges two sorted linked lists into one sorted linked list.
    """
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
        
    # Append the remaining nodes of list1 or list2
    current.next = list1 if list1 else list2
    
    return dummy.next

# Helper functions for testing
def create_linked_list(arr: list) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_array(head: Optional[ListNode]) -> list:
    res = []
    current = head
    while current:
        res.append(current.val)
        current = current.next
    return res

if __name__ == "__main__":
    # Test Example 1
    l1 = create_linked_list([1, 2, 4])
    l2 = create_linked_list([1, 3, 4])
    merged1 = mergeTwoLists(l1, l2)
    print("Example 1 Output:", linked_list_to_array(merged1))  # Expected: [1, 1, 2, 3, 4, 4]

    # Test Example 2
    l1 = create_linked_list([])
    l2 = create_linked_list([])
    merged2 = mergeTwoLists(l1, l2)
    print("Example 2 Output:", linked_list_to_array(merged2))  # Expected: []

    # Test Example 3
    l1 = create_linked_list([])
    l2 = create_linked_list([0])
    merged3 = mergeTwoLists(l1, l2)
    print("Example 3 Output:", linked_list_to_array(merged3))  # Expected: [0]
