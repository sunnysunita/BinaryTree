import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def height(root):
    # Find the Height Of Binary Tree
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return 0
    left_tree_height = height(root.left)
    right_tree_height = height(root.right)
    return max(left_tree_height, right_tree_height) + 1

def diameter(root):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return 0
    LH = height(root.left)
    RH = height(root.right)

    left_diameter = diameter(root.left)
    righ_diameter = diameter(root.right)

    return max(LH + RH + 1, max(left_diameter, righ_diameter))


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

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
print_binary_tree(root)
print(diameter(root))
# 1 2 3 4 5 -1 -1 6 -1 -1 7 8 -1 -1 9 -1 -1 -1 -1
