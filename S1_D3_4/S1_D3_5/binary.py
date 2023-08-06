class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def invert_binary_tree(root):
    if not root:
        return None

    # Swap the left and right children of the current node
    root.left, root.right = root.right, root.left

    # Recursively invert the left and right subtrees
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root
# Example usage:
# Let's create a binary tree as follows:
#        1
#       / \
#      2   3
#     / \ / \
#    4  5 6  7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Invert the binary tree
inverted_root = invert_binary_tree(root)
