# 1161. Maximum Level Sum of a Binary Tree

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the binary tree.

from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        lvl = 1
        max_sum = float('-inf')
        res = 1
        while q:
            lvl_sum = 0
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                lvl_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if lvl_sum > max_sum:
                max_sum = lvl_sum
                res = lvl
            lvl += 1
        return res

# Example usage:
root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)

s = Solution()
print(s.maxLevelSum(root))