class doublylinkNode:
    def __init__(self,val,next=None,prev=None):
        self.val=val
        self.next=next
        self.prev=prev
head=doublylinkNode(5)
a=doublylinkNode(1)
b=doublylinkNode(3)
def insert_at_beginning(head,val):
    new_node=doublylinkNode(val)
    new_node.next=head
    head.prev=new_node
    head=new_node
    return head
head=insert_at_beginning(head,Tail,3)
