class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:

    def __init__(self):
        self.root = None
        self.numNodes = 0

    def printTreeHelper(self, root):
        if root == None:
            return
        print(root.data, end = ":")
        if root.left != None:
            print("L:",end='')
            print(root.left.data,end=',')
        if root.right != None:
            print("R:",end='')
            print(root.right.data,end='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)

    def printTree(self):
        self.printTreeHelper(self.root)

    def searchhelp(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return True
        if data < root.data:
            return self.searchhelp(root.left, data)
        else:
            return self.searchhelp(root.right, data)


    def search(self, data):
        return self.searchhelp(self.root, data)
    def inserthelp(self, root, data):
        if root is None:
            return BinaryTreeNode(data)
        if data < root.data:
            root.left = self.inserthelp(root.left, data)
            return root
        else:
            root.right = self.inserthelp(root.right, data)
            return root
    def insert(self, data):
        self.numNodes += 1
        self.root = self.inserthelp(self.root, data)
    #Implement this function here
    def min(self, root):
        if root == None:
            return 100000
        if root.left == None:
            return root.data
        return self.min(root.left)
    def deletehelp(self, root, data):
        if root is None:
            return False, None
        if data < root.data:
            deleted, newleftnode = self.deletehelp(root.left, data)
            root.left = newleftnode
            return deleted, root
        if data > root.data:
            deleted, newrightnode = self.deletehelp(root.right, data)
            root.right = newrightnode
            return deleted, root
        if root.left == None and root.right == None:
            return True, None
        if root.left == None:
            return True, root.right
        if root.right == None:
            return True, root.left

        replacement = self.min(root.right)
        root.data = replacement
        deleted, newrightnode = self.deletehelp(root.right, replacement)
        root.right = newrightnode
        return True, root
    def delete(self, data):
        deleted, root = self.deletehelp(self.root, data)
        if deleted is True:
            self.numNodes -= 1
        return deleted
    #Implement this function here

    def count(self):
        return self.numNodes
b = BST()
li = [int(ele) for ele in input().split()]
i = 0
while(i < (len(li) )):
    choice = li[i]
    if choice == 1:
        data = li[i+1]
        b.insert(data)
        i+=2
    elif choice == 2:
        data = li[i+1]
        b.delete(data)
        i+=2
    elif choice == 3:
        data = li[i+1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
        i+=2
    else:
        b.printTree()
        i+=1

