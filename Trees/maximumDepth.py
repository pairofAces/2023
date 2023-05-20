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


# DFS - Iterative
class Solution2:
    def maxDepth(self, root:TreeNode):
        stack = [[root, 1]]
        res = 0

        while stack:
            node,depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        
        return res
    
# BFS

from collections import deque

class Solution3:
    def maxDepth(self, root: TreeNode):
        q = deque()
        
        if root:
            q.append(root)
        
        level = 0

        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                elif node.right:
                    q.append(node.right)
            level += 1
            
        return level
