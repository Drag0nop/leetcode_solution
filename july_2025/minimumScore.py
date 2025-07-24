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
from typing import List, Tuple
from collections import defaultdict
from itertools import combinations

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = defaultdict(list)
        
        # Build the graph
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Function to calculate the XOR of a component
        def dfs(node: int, visited: set) -> int:
            visited.add(node)
            val = nums[node]
            for i in graph[node]:
                if i not in visited:
                    val ^= dfs(i, visited)
            return val

        min_score = float('inf')

        # Try all pairs of edges to remove
        for (a1, b1), (a2, b2) in combinations(edges, 2):
            # Remove edges a1-b1 and a2-b2
            visited = set()
            val = []
            
            # Calculate the XOR for the first component
            val.append(dfs(a1, visited))
            val.append(dfs(b1, visited))
            
            # Calculate the XOR for the second component
            val.append(dfs(a2, visited))
            val.append(dfs(b2, visited))
            
            # Get the max and min XOR values
            max_xor = max(val)
            min_xor = min(val)
            
            # Update the minimum score
            min_score = min(min_score, max_xor - min_xor)

        return min_score

s = Solution()
print(s.minimumScore([1,5,5,4,11], [[0,1],[1,2],[1,3],[3,4]]))  # Output: 9