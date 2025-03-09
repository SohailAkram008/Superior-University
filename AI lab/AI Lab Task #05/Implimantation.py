class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def buildTree():
    root = TreeNode('A')
    root.left = TreeNode('B')
    root.right = TreeNode('C')
    root.left.left = TreeNode('D')
    root.left.right = TreeNode('E')
    root.right.left = TreeNode('F')
    root.left.right.left = TreeNode('G')
    return root

def inorderDFS(node, visited):
    if node is None:
        return
    inorderDFS(node.left, visited)
    visited.append(node.value)   
    inorderDFS(node.right, visited)

def preorderDFS(node, visited):
    if node is None:
        return
    visited.append(node.value)   
    preorderDFS(node.left, visited)
    preorderDFS(node.right, visited)

def postorderDFS(node, visited):
    if node is None:
        return
    postorderDFS(node.left, visited)
    postorderDFS(node.right, visited)
    visited.append(node.value)   

root = buildTree()
visited = []
inorderDFS(root, visited)
print("Inorder:", visited)   
visited = []
preorderDFS(root, visited)
print("Preorder:", visited)   
visited = []
postorderDFS(root, visited)
print("Postorder:", visited)   