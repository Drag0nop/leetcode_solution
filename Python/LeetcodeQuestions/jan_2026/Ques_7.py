# 1339. Maximum Product of Splitted Binary Tree

# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the binary tree.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        self.max_prod = 0

        # First DFS: get total sum
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)

        total = totalSum(root)

        # Second DFS: compute subtree sums and products
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            sub_sum = node.val + left + right

            # try cutting above this node
            self.max_prod = max(
                self.max_prod,
                sub_sum * (total - sub_sum)
            )

            return sub_sum

        dfs(root)
        return self.max_prod % MOD

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
s = Solution()
print(s.maxProduct(root)) # Output: 110