import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return
    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)

def find_leaf_node(root):
    if root is None:
        return 0
    LLN = find_leaf_node(root.left)
    RLN = find_leaf_node(root.right)
    if LLN == 0 and RLN == 0:
        return LLN + RLN + 1
    else:
        return LLN + RLN


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
print(find_leaf_node(root))
