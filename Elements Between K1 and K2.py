import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

"""def elementsInRangeK1K2(root, k1, k2, list):
    if root is None:
        return list
    if root.data > k2:
        elementsInRangeK1K2(root.left, k1, k2, list)
    if root.data < k1:
        elementsInRangeK1K2(root.right, k1, k2, list)
    else:
        # print(root.data, end=" ")
        list.append(root.data)
        elementsInRangeK1K2(root.left, k1, k2, list)
        elementsInRangeK1K2(root.right, k1, k2, list)
    return list"""
def elementsInRangeK1K2(root, k1, k2):
    if root is None:
        return []
    if root.data >= k1 and root.data <= k2:
        list = []
        list.append(root.data)
        lst = elementsInRangeK1K2(root.left, k1, k2)
        rst = elementsInRangeK1K2(root.right, k1, k2)
        list.extend(lst)
        list.extend(rst)
        return list

    elif root.data > k2:
        return elementsInRangeK1K2(root.left, k1, k2)
    else:
        # root.data < k1:
        return elementsInRangeK1K2(root.right, k1, k2)

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
k1, k2 = (int(i) for i in input().strip().split())
list1 = elementsInRangeK1K2(root, k1, k2)
list1.sort()
for e in list1:
    print(e, end=" ")
