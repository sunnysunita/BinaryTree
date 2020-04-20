class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
btn1 = BinaryTreeNode(10)
btn2 = BinaryTreeNode(20)
btn3 = BinaryTreeNode(30)
btn4 = BinaryTreeNode(40)
btn1.left = btn2
btn1.right = btn3
btn2.left = btn4

#print(btn1.data, btn1.left.data, btn1.right.data, btn1.left.left.data)
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

def input_tree():
    root_data = int(input())
    if root_data == -1:
        return None
    root_node = BinaryTreeNode(root_data)
    left_tree = input_tree()
    right_tree = input_tree()
    root_node.left = left_tree
    root_node.right = right_tree
    return root_node

root = input_tree()
print_binary_tree(root)

