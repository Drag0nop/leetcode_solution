from collections import Counter
import math

def getSmallestBaseSegment(segmentSize, missingData):
    freq = Counter(missingData)

    # If there are more distinct required characters
    # than positions available in the base segment,
    # no solution exists.
    if len(freq) > segmentSize:
        return "-1"

    # Check whether k replications are sufficient
    def possible(k):
        required = 0

        for count in freq.values():
            required += (count + k - 1) // k

            if required > segmentSize:
                return False

        return True

    # Binary search for minimum number of replications
    low = 1
    high = max(freq.values())

    while low < high:
        mid = (low + high) // 2

        if possible(mid):
            high = mid
        else:
            low = mid + 1

    k = low

    # Construct lexicographically smallest base segment
    result = []

    for ch in sorted(freq):
        count_needed = (freq[ch] + k - 1) // k
        result.extend([ch] * count_needed)

    # Fill remaining positions.
    # Assuming extra positions can use the smallest
    # character occurring in missingData.
    while len(result) < segmentSize:
        result.append(min(freq))

    return ''.join(result)

segmentSize = 4
missingData = "abacabac"
print(getSmallestBaseSegment(segmentSize, missingData))  # Output: "aabc"