from queue import Queue

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_binary_tree(root):
    if root is None:
        return
    else:
        print(root.data, end=":")
        if root.left != None:
            print("L", root.left.data, end=", ")
        if root.right != None:
            print("R", root.right.data, end="")
        print()
        print_binary_tree(root.left)
        print_binary_tree(root.right)

def take_level_input():
    root_data = int(input("enter the root value: "))
    if root_data is -1:
        return None
    root = BinaryTree(root_data)
    q = Queue()
    q.put(root)
    while q.empty() is False:
        curr = q.get()
        left_data = int(input("enter the left child of"+str(curr.data)+":"))
        if left_data is not -1:
            left_child = BinaryTree(left_data)
            curr.left = left_child
            q.put(left_child)

        right_data = int(input("enter the right child of"+str(curr.data)+":"))
        if right_data is not -1:
            right_child = BinaryTree(right_data)
            curr.right = right_child
            q.put(right_child)
    return root
root = take_level_input()
print_binary_tree(root)

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1