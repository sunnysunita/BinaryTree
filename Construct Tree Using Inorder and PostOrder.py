import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePostOrder(postorder, inorder):
    if len(postorder) == 0 or len(inorder) == 0:
        return None

    root_data = postorder[-1]
    root = BinaryTreeNode(root_data)

    if len(postorder) == 1 and len(inorder) == 1:
        return root


    index_of_root = inorder.index(root_data)


    lst_inorder = inorder[:index_of_root]

    if index_of_root+1 >= len(inorder):
        rst_inorder = []
    else:
        rst_inorder = inorder[index_of_root+1:]

    lst_postorder = postorder[:len(lst_inorder)]

    if len(rst_inorder) == 0:
        rst_postorder = []
    else:
        rst_postorder = postorder[len(lst_inorder):-1]

    left_sub_tree = buildTreePostOrder(lst_postorder, lst_inorder)
    right_sub_tree = buildTreePostOrder(rst_postorder, rst_inorder)
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
postOrder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePostOrder(postOrder, inorder)
printLevelATNewLine(root)
