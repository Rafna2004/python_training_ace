class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    """
    Given the head of a sorted linked list, delete all duplicates 
    such that each element appears only once.
    Returns the updated sorted linked list.
    """
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next  # Skip duplicate
        else:
            current = current.next  # Move forward
    return head

def print_list(head: ListNode):
    nodes = []
    current = head
    while current:
        nodes.append(str(current.val))
        current = current.next
    print(" -> ".join(nodes) if nodes else "None")

# Example Usage & Verification:
if __name__ == "__main__":
    # Example 1: 1 -> 1 -> 2
    head1 = ListNode(1, ListNode(1, ListNode(2)))
    print("Original 1:", end=" ")
    print_list(head1)
    head1 = deleteDuplicates(head1)
    print("Result 1:  ", end=" ")
    print_list(head1)

    print()

    # Example 2: 1 -> 1 -> 2 -> 3 -> 3
    head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    print("Original 2:", end=" ")
    print_list(head2)
    head2 = deleteDuplicates(head2)
    print("Result 2:  ", end=" ")
    print_list(head2)
