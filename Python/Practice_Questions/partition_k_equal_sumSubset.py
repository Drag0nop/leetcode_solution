def canPartitionKSubsets(nums, k):
    total = sum(nums)
    if total % k != 0: return False
    target = total // k
    nums.sort(reverse=True)
    if nums[0] > target: return False
    dp = [False] * len(nums)

    def backtrack(start, current_sum, count):
        if count == k - 1:
            return True
        if current_sum == target:
            return backtrack(0, 0, count + 1)
        prev = -1
        for i in range(start, len(nums)):
            if dp[i] or current_sum + nums[i] > target or nums[i] == prev:
                continue
            dp[i] = True
            if backtrack(i + 1, current_sum + nums[i], count):
                return True
            dp[i] = False
            prev = nums[i]
            if current_sum == 0:
                break
        
        return False
    return backtrack(0, 0, 0)

# Example Usage:
nums = [4,3,2,3,5,2,1]
k = 4
print(canPartitionKSubsets(nums, k))  # Output: True