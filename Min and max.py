#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

INT_MIN = -2147483648
INT_MAX = 2147483647
# Problem ID 1567, Find the minimum and maximum value
def minMax(root):
    # Given a binary tree, find and return the min and max data value of given
    # binary tree. Return maximum and minimum from this function only. Largest
    # and smallest data possible is provided through INT_MAX and INT_MIN
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return INT_MAX, INT_MIN

    lstmin, lstmax = minMax(root.left)
    rstmin, rstmax = minMax(root.right)
    return min(root.data, lstmin, rstmin), max(root.data, lstmax, rstmax)

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0] == -1:
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
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
minimum, maximum = minMax(root)
print(maximum, minimum)

