"""
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.
You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.
Return the maximum number of events you can attend.

Example 1:

Input: events = [[1,2],[2,3],[3,4]]
Output: 3

Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
"""

# time complexity -> O(nlog(n)), space complexity -> O(n)

import heapq
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        mx = max(e for s, e in events)
        events.sort()
        min_heap = []
        res = j = 0
        for i in range(1, mx + 1):
            while j < len(events) and events[j][0] == i:
                heapq.heappush(min_heap, events[j][1])
                j += 1
            while min_heap and i > min_heap[0]:
                heapq.heappop(min_heap)
            if min_heap and i <= min_heap[0]:
                heapq.heappop(min_heap)
                res += 1
        return res


print(Solution().maxEvents([[1,2], [2,3], [3,4]])) # Output: 3