import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return
    q = queue.Queue()
    q.put(root)
    q.put("Nil")
    while q.empty() is False:
        curr = q.get()
        if curr is not "Nil":
            print(curr.data, end=" ")
            if curr.left is not None:
                q.put(curr.left)
            if curr.right is not None:
                q.put(curr.right)

        else:
            print()
            if q.empty() is True:
                break
            else:
                q.put("Nil")

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
#n=int(input())
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
printLevelATNewLine(root)
