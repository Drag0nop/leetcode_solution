# 1233. Remove Sub-Folders from the Filesystem

"""
given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.

If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], 
followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".

The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

Example :

Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
"""

# Time complexity: O(n log n) for sorting.
# Space complexity: O(n) for storing the result.

from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()  #sort lexicographically
        res = []
        
        for i in folder:
            if not res or not i.startswith(res[-1] + "/"):
                res.append(i)
        
        return res

s = Solution()
print(s.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))  # output: ["/a", "/c/d", "/c/f"]