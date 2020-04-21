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


def buildLevelTree():

    root = BinaryTreeNode(int(input()))
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = int(input())
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = int(input())
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
root = buildLevelTree()
print(height(root))