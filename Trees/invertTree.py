# LC 226 - Invert Binary Tree 

# Given the root of a binary tree, invert the tree, and return it's root

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time Complexity: O(n), where (n) is the number of nodes
# Space Complexity:
    # Worst case: O(n), where (n) is the number of recursive calls that 
    # need to be performed, per node.

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # base case
        if not root:
            return None
        
        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        # also, to avoide the 'tmp' variable-> root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
