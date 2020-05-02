import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printkDistanceNodeDown(root, k):

    # Base Case
    if root is None or k< 0 :
        return

        # If we reach a k distant node, print it
    if k == 0 :
        print(root.data)
        return

        # Recur for left and right subtee
    printkDistanceNodeDown(root.left, k-1)
    printkDistanceNodeDown(root.right, k-1)


# Prints all nodes at distance k from a given target node
# The k distant nodes may be upward or downward. This function
# returns distance of root from target node, it returns -1
# if target node is not present in tree rooted with root
def printkDistanceNode(root, target, k):

    # Base Case 1 : IF tree is empty return -1
    if root is None:
        return -1

    # If target is same as root. Use the downward function
    # to print all nodes at distance k in subtree rooted with
    # target or root
    if root == target:
        printkDistanceNodeDown(root, k)
        return 0

        # Recur for left subtree
    dl = printkDistanceNode(root.left, target, k)

    # Check if target node was found in left subtree
    if dl != -1:

        # If root is at distance k from target, print root
        # Note: dl is distance of root's left child
        # from target
        if dl +1 == k :
            print(root.data)

            # Else go to right subtreee and print all k-dl-2
        # distant nodes
        # Note: that the right child is 2 edges away from
        # left chlid
        else:
            printkDistanceNodeDown(root.right, k-dl-2)

            # Add 1 to the distance and return value for
        # for parent calls
        return 1 + dl

        # MIRROR OF ABOVE CODE FOR RIGHT SUBTREE
    # Note that we reach here only when node was not found
    # in left subtree
    dr = printkDistanceNode(root.right, target, k)
    if dr != -1:
        if (dr+1 == k):
            print(root.data)
        else:
            printkDistanceNodeDown(root.left, k-dr-2)
        return 1 + dr

        # If target was neither present in left nor in right subtree
    return -1

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
def find_node(root, k):
    if root is None:
        return None
    if root.data == k:
        return root
    lst = find_node(root.left, k)
    rst = find_node(root.right, k)
    if lst is None and rst is None:
        return None
    elif lst is not None:
        return lst
    elif rst is not None:
        return rst

list = [int(e) for e in input().split()]
target = int(input())
k = int(input())
root = buildLevelTree(list)
target = find_node(root, target)
#printLevelWise(root)
printkDistanceNode(root, target, k)

