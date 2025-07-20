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
from typing import List, Dict, Set

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        folder_map: Dict[str, Set[str]] = {}
        for path in paths:
            folder = '/'.join(path)
            folder_map[folder] = set(path)

        marked_folders = set()
        for folder1 in folder_map:
            if folder1 in marked_folders:
                continue
            for folder2 in folder_map:
                if folder1 != folder2 and folder_map[folder1] == folder_map[folder2]:
                    marked_folders.add(folder2)

        result = []
        for path in paths:
            if '/'.join(path) not in marked_folders:
                result.append(path)

        return result

s = Solution()
print(s.deleteDuplicateFolder([["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]))