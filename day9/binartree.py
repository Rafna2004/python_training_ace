class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
A=TreeNode(1)
B=TreeNode(2)
C=TreeNode(3)
D=TreeNode(4)
E=TreeNode(5)
F=TreeNode(10)
A.left=B
A.right=C
B.left=D
B.right=E
C.left=F
print(A.val)
print(B.val)
print(C.val)
print(D.val)
print(E.val)
print(F.val)
def pre_order(node):
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)
pre_order(A)    

def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node)
    in_order(node.right)
in_order(A)    