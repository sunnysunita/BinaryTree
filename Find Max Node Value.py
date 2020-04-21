def find_max(root):
    if root is None:
        return -1
    left_tree_max = find_max(root.left)
    right_tree_max = find_max(root.right)
    return max(left_tree_max, right_tree_max, root.data)

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):
    # Given a binary tree, print the postorder traversal of given tree.
    # Post-order traversal is: LeftChild RightChild Root
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return
    inOrder(root.left)
    print(root.data, end=" ")
    inOrder(root.right)


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
print(find_max(root))
