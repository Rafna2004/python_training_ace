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

# Traverse and print the Linked List
temp = head
while temp:
    print(temp.val, end=" -> ")
    temp = temp.next
print("None")

