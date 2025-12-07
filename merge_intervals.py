# LC question no. 56

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        start,end = intervals[0]
        for i in range(1, len(intervals)):
            newStart,newEnd = intervals[i]

            if end < newStart:
                res.append([start,end])
                start,end = intervals[i]
            else:
                end = max(end, newEnd)
        res.append([start,end])
        return res

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))  # Output: [[1,6],[8,10],[15,18]]