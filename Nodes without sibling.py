import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def nodesWithoutSibling(root):
    # Given a binary tree, print all nodes that don’t have a sibling. Print the
    # elements in different lines. And order of elements doesn't matter.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return None
    left_tree = nodesWithoutSibling(root.left)
    right_tree = nodesWithoutSibling(root.right)
    if left_tree is None and right_tree is True:
        print(root.right.data)
        return True
    elif left_tree is True and right_tree is None:
        print(root.left.data)
        return True
    elif left_tree is None and right_tree is None:
        return True
    elif right_tree is True and left_tree is True:
        return True

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
val = nodesWithoutSibling(root)
