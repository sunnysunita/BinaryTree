import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(list, floor, ceiling):
    if floor > ceiling:
        return None
    mid_index = (floor+ceiling)//2
    root = BinaryTreeNode(list[mid_index])
    lst = constructBST(list, floor, mid_index-1)
    rst = constructBST(list, mid_index+1, ceiling)
    root.left = lst
    root.right = rst
    return root
def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
lst=[int(i) for i in input().strip().split()]
root= constructBST(lst, floor=0, ceiling=len(lst)-1)
preOrder(root)
