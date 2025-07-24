"""
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 0-indexed integer array nums of length n where nums[i] represents the value of the ith node. You are also given a 2D integer array edges of length 
n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Remove two distinct edges of the tree to form three connected components. For a pair of removed edges, the following steps are defined:

Get the XOR of all the values of the nodes for each of the three components respectively.
The difference between the largest XOR value and the smallest XOR value is the score of the pair.
For example, say the three components have the node values: [4,5,7], [1,9], and [3,3,3]. The three XOR values are 4 ^ 5 ^ 7 = 6, 1 ^ 9 = 8, and 3 ^ 3 ^ 3 = 3. 
The largest XOR value is 8 and the smallest XOR value is 3. The score is then 8 - 3 = 5.
Return the minimum score of any possible pair of edge removals on the given tree.

Example :

Input: nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]
Output: 9
Explanation: The diagram above shows a way to make a pair of removals.
- The 1st component has nodes [1,3,4] with values [5,4,11]. Its XOR value is 5 ^ 4 ^ 11 = 10.
- The 2nd component has node [0] with value [1]. Its XOR value is 1 = 1.
- The 3rd component has node [2] with value [5]. Its XOR value is 5 = 5.
The score is the difference between the largest and smallest XOR value which is 10 - 1 = 9.
It can be shown that no other pair of removals will obtain a smaller score than 9.
"""

from collections import defaultdict
from typing import List

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = defaultdict(list)
        
        # Build the graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        xor = [0] * n
        parent = [-1] * n
        in_time = [0] * n
        out_time = [0] * n
        time = 0

        # DFS to compute XOR values, parent, and Euler in/out time
        def dfs(node: int, par: int):
            nonlocal time
            in_time[node] = time
            time += 1

            xor[node] = nums[node]
            parent[node] = par
            for i in graph[node]:
                if i == par:
                    continue
                dfs(i, node)
                xor[node] ^= xor[i]

            out_time[node] = time
            time += 1

        dfs(0, -1)

        total = xor[0]
        res = float('inf')

        # Check if u is an ancestor of v
        def is_ancestor(u: int, v: int) -> bool:
            return in_time[u] <= in_time[v] and out_time[v] <= out_time[u]

        # Try all pairs of nodes (which are endpoints of edges to remove)
        for i in range(1, n):
            for j in range(i + 1, n):
                if is_ancestor(i, j):
                    a = xor[j]
                    b = xor[i] ^ xor[j]
                    c = total ^ xor[i]
                elif is_ancestor(j, i):
                    a = xor[i]
                    b = xor[j] ^ xor[i]
                    c = total ^ xor[j]
                else:
                    a = xor[i]
                    b = xor[j]
                    c = total ^ xor[i] ^ xor[j]

                res = min(res, max(a, b, c) - min(a, b, c))

        return res

s = Solution()
print(s.minimumScore([1,5,5,4,11], [[0,1],[1,2],[1,3],[3,4]]))  # Output: 9