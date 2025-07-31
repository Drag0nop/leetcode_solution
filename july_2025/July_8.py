# 1751. Maximum Number of Events That Can Be Attended 2

"""
You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, 
and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. 
Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

Return the maximum sum of values that you can receive by attending events.

Example:

Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
Output: 10
Explanation: Choose event 2 for a total value of 10.
Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.
"""
# use dp + binary search
from typing import List
from bisect import bisect_right

# option 1 (ok approach)
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])

        dp = [[0] * (k + 1) for _ in range(len(events) + 1)]

        for i in range(1, len(events) + 1):
            l, r = 0, i - 1
            prev = 0
            while l < r:
                mid = l + (r - l) // 2
                if events[mid][1] < events[i - 1][0]:
                    l = mid + 1
                else:
                    r = mid
            prev = l - 1 if events[l][1] < events[i - 1][0] else l - 1

            for j in range(1, k + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j])   # Skip current event
                if prev >= 0:
                    dp[i][j] = max(dp[i][j], dp[prev + 1][j - 1] + events[i - 1][2])
                else:
                    dp[i][j] = max(dp[i][j], events[i - 1][2])
        return dp[len(events)][k]


# option 2 (better approach and optimize)
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])

        end_times = [event[1] for event in events]

        dp = [[0] * (k + 1) for _ in range(len(events) + 1)]

        for i in range(1, len(events) + 1):
            # Find index of last event that ends < current start
            prev_index = bisect_right(end_times, events[i - 1][0] - 1)

            for j in range(1, k + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j])   # Skip current event
                # Attend current event
                dp[i][j] = max(dp[i][j], dp[prev_index][j - 1] + events[i - 1][2])

        return dp[len(events)][k]


print(Solution().maxValue([[1,3,4],[2,4,3],[3,6,5],[4,5,6]], 2)) # Output: 10