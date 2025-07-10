"""
You are given an integer eventTime denoting the duration of an event. You are also given two integer arrays startTime and endTime, each of length n.

These represent the start and end times of n non-overlapping meetings that occur during the event between time t = 0 and time t = eventTime, 
where the ith meeting occurs during the time [startTime[i], endTime[i]].

You can reschedule at most one meeting by moving its start time while maintaining the same duration, such that the meetings remain non-overlapping, 
to maximize the longest continuous period of free time during the event.

Return the maximum amount of free time possible after rearranging the meetings.

Note that the meetings can not be rescheduled to a time outside the event and they should remain non-overlapping.

Note: In this version, it is valid for the relative ordering of the meetings to change after rescheduling one meeting.

Example :

Input: eventTime = 5, startTime = [1,3], endTime = [2,5]

Output: 2

Explanation:
Reschedule the meeting at [1, 2] to [2, 3], leaving no meetings during the time [0, 2].
"""

#  complexity -> O(n)
from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        space = [False] * n

        s1 =  0
        for i in range(n):
            if endTime[i] - startTime[i] <= s1: space[i] = True
            s1 = max(s1, startTime[i] - (0 if i == 0 else endTime[i - 1]))
        
        s2 = 0
        for i in range(n - 1, -1, -1):
            if endTime[i] - startTime[i] <= s2: space[i] = True
            s2 = max(s2,(eventTime if i == n - 1 else startTime[i + 1]) - endTime[i])
        
        res = 0
        for i in range(n):
            l = 0 if i == 0 else endTime[i - 1]
            r = eventTime if i == n - 1 else startTime[i + 1]
            if space[i]:
                res = max(res, r - l)
            else:
                res = max(res, r - l - (endTime[i] - startTime[i]))

        return res 

print(Solution().maxFreeTime(5, [1,3], [2,5])) #output 2