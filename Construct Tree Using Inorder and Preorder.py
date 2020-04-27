import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePreOrder(preorder, inorder):
    if len(preorder) == 0 or len(inorder) == 0:
        return None

    root_data = preorder[0]
    root = BinaryTreeNode(root_data)

    if len(preorder) == 1 and len(inorder) == 1:
        return root


    index_of_root = inorder.index(root_data)


    lst_inorder = inorder[:index_of_root]

    if index_of_root+1 >= len(inorder):
        rst_inorder = []
    else:
        rst_inorder = inorder[index_of_root+1:]

    lst_preorder = preorder[1:1+len(lst_inorder)]

    if len(rst_inorder) == 0:
        rst_preorder = []
    else:
        rst_preorder = preorder[1+len(lst_inorder):]

    left_sub_tree = buildTreePreOrder(lst_preorder, lst_inorder)
    right_sub_tree = buildTreePreOrder(rst_preorder, rst_inorder)
    root.left = left_sub_tree
    root.right = right_sub_tree
    return root

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
n=int(input())
preorder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePreOrder(preorder, inorder)
printLevelATNewLine(root)
# 7
# 1 2 4 5 3 6 7
# 4 2 5 1 6 3 7