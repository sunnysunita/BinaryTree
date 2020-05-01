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
k=int(input())
lst = rootToLeafPathsSumToK(root, k, [])
for e in lst:
    if isinstance(e, list) is True:
        for i in e:
            print(i, end=" ")
        print()
    else:
        print(e, end=" ")
