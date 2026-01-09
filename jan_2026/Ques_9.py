# 865. Smallest Subtree with all the Deepest Nodes

# Complexity Analysis:
# Time Complexity: O(N), where N is the number of nodes in the tree.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return 0, None

            ld, ln = dfs(node.left)
            rd, rn = dfs(node.right)

            if ld > rd:
                return ld + 1, ln
            elif rd > ld:
                return rd + 1, rn
            else:
                return ld + 1, node

        return dfs(root)[1]

# Example usage:
s = Solution()
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
s = Solution()
print(s.subtreeWithAllDeepest(root).val)  # Output: 3