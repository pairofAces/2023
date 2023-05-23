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
    # Time Complexity: O(n), where (n) is the number of nodes in the binary tree. Because we visit each node
    #                  once during the recursion.

    # Space Complexity: O(h), where (h) is the height of the binary tree. This is because, in the worst
    #                   case, the height of the tree becomes equal to the number of nodes in the tree.
class Solution:
    def maxDepth(self, root: TreeNode):
        # base case
        if not root:
            return
        
        return 1 + (max(self.maxDepth(root.left), self.maxDepth(root.right)))


# DFS - Iterative
    # Time Complexity: O(n), where (n) is the number of nodes in the binary tree
    
    # Space Complexity: O(n), where (n) is the number of nodes in the tree. This is because
    #                   in the worst case, the stack can contain all nodes on one side of the
    #                   tree, resulting in a skewed tree.

    # In this solution, a stack (implemented as a linked list) is used.
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

    # Time Complexity: O(n), where (n) is the number of nodes in the tree
    
    # Space Complexity: O(n), where (n) is the number of nodes in the tree. This is because
    #                   in the worst case, the maximum number of nodes in the queue during the 
    #                   BFS traversal will be equal to the number of nodes in the tree. This is due
    #                   to a completely unbalanced tree, which resembles a linked list, and occurs if
    #                   each node only has a right child or a left child.

    # In this solution, a queue (implemented as a deque) is used.
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
