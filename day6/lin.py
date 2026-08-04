class linkNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

head = linkNode(5)    
a = linkNode(1)
b = linkNode(3)
c = linkNode(4)
d = linkNode(7)

head.next = a
a.next = b  
b.next = c
c.next = d


temp = head
while temp:
    print(temp.val, end=" -> ")
    temp = temp.next
print("None")


def is_present(head, target):
    temp = head
    while temp:
        if temp.val == target:
            return True
        temp = temp.next
    return False

target = int(input("Enter number to search: "))
if is_present(head, target):
    print(f"Number {target} is present in the linked list.")
else:
    print(f"Number {target} is NOT present in the linked list.")


