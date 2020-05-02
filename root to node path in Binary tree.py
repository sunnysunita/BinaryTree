import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelWise(root):
    # Given a binary tree, print the tree in level wise order. For printing
    # a node with data N, you need to follow the exact format:
    # N:L:x,R:y
    # wherer, N is data of any node present in the binary tree. x and y are the
    # values of left and right child of node N. Print -1. if any child is null.
    # There is no space in between. You need to print all nodes in the level
    # order form in different lines.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return
    q = queue.Queue()
    q.put(root)
    while q.empty() is False:
        curr = q.get()
        print(str(curr.data), end=":")
        if curr.left is not None:
            q.put(curr.left)
            print("L:"+str(curr.left.data), end=",")
        else:
            print("L:-1", end=",")
        if curr.right is not None:
            q.put(curr.right)
            print("R:"+str(curr.right.data))
        else:
            print("R:-1")


# 1 2 3 4 5 -1 -1 -1 -1 -1 -1



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
def print_to_node(root, data):
    if root is None:
        return None
    if root.data == data:
        return [root.data]
    lst = print_to_node(root.left, data)
    if lst is not None:
        lst.append(root.data)
        return lst
    rst = print_to_node(root.right, data)
    if rst is not None:
        rst.append(root.data)
        return rst
    return None


# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
printLevelWise(root)
data = 3
list = print_to_node(root, data)
print(list)