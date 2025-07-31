# 1948. Delete Duplicate Folders in System

"""
Due to a bug, there are many duplicate folders in a file system. You are given a 2D array paths, 
where paths[i] is an array representing an absolute path to the ith folder in the file system.

For example, ["one", "two", "three"] represents the path "/one/two/three".
Two folders (not necessarily on the same level) are identical if they contain the same non-empty set of identical subfolders and underlying subfolder structure. 
The folders do not need to be at the root level to be identical. If two or more folders are identical, then mark the folders as well as all their subfolders.

However, if the file structure also included the path "/b/w", then the folders "/a" and "/b" would not be identical. Note that "/a/x" and "/b/x" would still be
considered identical even with the added folder.
Once all the identical folders and their subfolders have been marked, the file system will delete all of them. The file system only runs the deletion once, 
so any folders that become identical after the initial deletion are not deleted.

Return the 2D array ans containing the paths of the remaining folders after deleting all the marked folders. The paths may be returned in any order.

Example :

Input: paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
Output: [["d"],["d","a"]]

Explanation: The file structure is as shown.
Folders "/a" and "/c" (and their subfolders) are marked for deletion because they both contain an empty
folder named "b".
"""

from typing import List, Dict
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.name = ""
        self.to_delete = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()
        
        # Step 1: Build Trie
        for path in paths:
            node = root
            for i in path:
                if i not in node.children:
                    node.children[i] = TrieNode()
                    node.children[i].name = i
                node = node.children[i]

        # Step 2: Serialize subtrees and find duplicates
        sub_map = defaultdict(list)
        
        def serialize(node):
            if not node.children:
                return ""
            serial = []
            for child in sorted(node.children):
                serial.append(child + "(" + serialize(node.children[child]) + ")")
            s = "".join(serial)
            sub_map[s].append(node)
            return s

        serialize(root)

        # Step 3: Mark duplicates for deletion
        for nodes in sub_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.to_delete = True

        # Step 4: Collect result
        res = []

        def dfs(node, path):
            for name, child in node.children.items():
                if not child.to_delete:
                    res.append(path + [name])
                    dfs(child, path + [name])

        dfs(root, [])
        return res


s = Solution()
print(s.deleteDuplicateFolder([["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]))


"""
class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        tree = {}
        for path in paths:
            node = tree
            for folder in path:
                node = node.setdefault(folder, {})
        
        duplicates = defaultdict(list)

        def serialize(node):
            if not node:
                return "()"

            child_s = "".join(child + serialize(child_node) for child, child_node in sorted(node.items()))

            serial = "(" + child_s + ")"
            duplicates[serial].append(node)
            return serial
        
        serialize(tree)

        for nodes in duplicates.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.clear()
                    node["#"] = True
        
        ret = []
        def collect_paths(node, path):
            for child_name, child_node in node.items():
                if "#" in child_node:
                    continue
                new_path = path + [child_name]
                ret.append(new_path)
                collect_paths(child_node, new_path)
        
        collect_paths(tree, [])
        return ret
"""