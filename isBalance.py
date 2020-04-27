import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def mirrorBinaryTree(root):
    # Mirror the given binary tree. That is, right child of every nodes should
    # become left and left should become right.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return
    if root.left is None and root.right is None:
        return
    mirrorBinaryTree(root.left)
    mirrorBinaryTree(root.right)
    root.left, root.right = root.right, root.left
    return root


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

def balance_tree(root):
    if root is None:
        return True
    height_LT = height(root.left)
    height_RT = height(root.right)
    if height_LT - height_RT > 1 or height_RT - height_LT > 1:
        return False
    left_BT = balance_tree(root.left)
    right_BT = balance_tree(root.right)
    if left_BT and right_BT:
        return True
    else:
        return False

def isBalance(root):
    if root is None:
        return 0, True
    LH, leftBalance = isBalance(root.left)
    RH, rightBalance = isBalance(root.right)
    h = 1 + max(LH, RH)
    if LH - RH > 1 or RH - LH > 1:
        return h, False
    if (leftBalance and rightBalance) is True:
        return h, True
    else:
        return h, False


# Problem ID 353, Level order traversal
def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
print(isBalance(root))
