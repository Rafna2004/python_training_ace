class queue:
    def __init__(self):
       q=[]
    def enqueue(self,new,q):
        q.append(new)

from collections import deque
class queue:  
    def __init__(self):
        self.items = deque()
        print("queue(using queue)created")

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}| Queue: {list(self.items)}")
    def dequeue(self):
        if not self.items:
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.items.popleft()
        print(f"Dequeued: {item}| Queue: {list(self.items)}")
        return item
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def peek(self):
        if not self.items:
            print("Queue is empty. Cannot peek.")
            return None
        item = self.items[0]
        print(f"Peek: {item}")
        return item
    def is_full(self, max_size):
        return len(self.items) >= max_size
    def display(self):
        if self.items:
            print(f"Queue(front-rear): {list(self.items)}")
        else:
            print("Queue is empty")
eq=queue()            
eq.enqueue("Alice")
eq.enqueue("Bob")
eq.enqueue("Charlie")
eq.enqueue("davi")
eq.display()
