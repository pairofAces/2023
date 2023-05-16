# LC 104 - Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the 
# longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive solution
class Solution:
    def maxDepth(self, root: TreeNode):
        # base case
        if not root:
            return
        
        return 1 + (max(self.maxDepth(self.left), self.maxDepth(self.right)))