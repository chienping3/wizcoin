class TreeNode():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val)
        if self.right:
            self.right.inorder()
            
def insertList(data, root, i=0):
    n = len(data)
    if i < n:
        tmp = TreeNode(data[i])
        root = tmp
        root.left = insertList(data, root.left, 2*i+1)
        root.right = insertList(data, root.right, 2*i+2)
    return root
            
datas = list(range(0, 10))
tree = TreeNode(datas[0])
# tree.left = TreeNode(datas[1])
# tree.right = TreeNode(datas[2])
# tree.left.left = TreeNode(datas[3])
# tree.left.right = TreeNode(datas[4])
# tree.right.left = TreeNode(datas[5])
tree = insertList(datas, tree, 0)
tree.inorder()