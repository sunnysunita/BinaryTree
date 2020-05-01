import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def rootToLeafPathsSumToK(root, k, list):

    if root is None:
        return []

    if root.left is None and root.right is None:
        if root.data == k:
            list.append(root.data)
            return list
        else:
            return []


    if root.data > k:
        return []



    list.append(root.data)
    k = k - root.data
    l = len(list)
    lst = rootToLeafPathsSumToK(root.left, k, list[:l])
    rst = rootToLeafPathsSumToK(root.right, k, list[:l])
    if len(lst) == 0 and len(rst) == 0:
        return []
    elif len(rst) == 0:
        return lst
    elif len(lst) == 0:
        return rst
    else:
        return [lst, rst]

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

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k=int(input())
"""lst = rootToLeafPathsSumToK(root, k, [])
for e in lst:
    if isinstance(e, list) is True:
        for i in e:
            print(i, end=" ")
        print()
    else:
        print(e, end=" ")"""
out = find_node(root, k)
printLevelWise(out)