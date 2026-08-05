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
int=4
temp=head.next
flag=0
while temp:
    if temp.val==int:
        flag=1
        break
    temp=temp.next
print(flag)    

