import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
INT_MIN = -100000
INT_MAX = 100000
def check_BST(root):
    if root is None:
        return INT_MAX, INT_MIN, True

    min_lst, max_lst, x = check_BST(root.left)
    min_rst, max_rst, y = check_BST(root.right)

    minimum = min(min_lst, min_rst, root.data)
    maximum = max(max_lst, max_rst, root.data)
    temp = True
    if root.data <= min_lst or root.data > max_rst:
        temp = False
    if x is not True or y is not True:
        temp = False

    return minimum, maximum, temp






def constructBST(list, floor, ceiling):
    if floor > ceiling:
        return
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
# preOrder(root)
min, max, bool = check_BST(root)
print(bool)