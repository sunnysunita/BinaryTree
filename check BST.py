import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
INT_MIN = -100000
INT_MAX = 100000

def lst_min(root):
    if root is None:
        return INT_MAX
    lst_min_val = lst_min(root.left)
    return min(root.data, lst_min_val)

def rst_max(root):
    if root is None:
        return INT_MIN
    rst_max_val = rst_max(root.right)
    return max(root.data, rst_max_val)


def check_BST(root):
    if root is None:
        return True
    lst = lst_min(root.left)
    rst = rst_max(root.right)
    if root.data > lst and root.data <= rst:
        return True
    else:
        return False


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
root = constructBST(lst, floor=0, ceiling=len(lst)-1)
print(check_BST(root))