class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class Solution:
    def insert(self, root, key):  # If empty tree,create newnode & return
        if root is None:
            return Node(key)

        if root.data == key:  # If key already present return root
            return root

        if key < root.data:
            if root.left:
                root.left = self.insert(root.left, key)
            else:
                root.left = Node(key)
        else:
            if root.right:
                root.right = self.insert(root.right, key)
            else:
                root.right = Node(key)

        return root


def inorder(root):  # Inorder tree traversal
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)


def preorder(root):  # PreOrder tree traversal
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)


def postorder(root):  # PostOrder tree traversal
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')


k = Node(15)
lst = [10, 18, 4, 11, 16, 20, 13]
obj = Solution()
for i in range(len(lst)):
    obj.insert(k, lst[i])
print('inorder: ', end="")
inorder(k)
print()
print('preorder :', end="")
preorder(k)
print()
print('postorder :', end="")
postorder(k)

#         15
#   10         18
# 4    11     16   20
#       13


