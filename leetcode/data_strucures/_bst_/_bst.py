import random
import bst


tree = bst.BST()

for _ in range(10):
    a = random.randint(1, 99)
    tree.insert(a)

print(tree.traverse(mode='inorder'))
