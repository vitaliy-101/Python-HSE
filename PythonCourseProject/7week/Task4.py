# https://leetcode.com/problems/frequency-of-the-most-frequent-element/submissions/1484542606/?envType=problem-list-v2&envId=sliding-window
def maxFrequency(nums, k):
    nums.sort()
    total = 0
    left = 0
    res = 0

    for r in range(len(nums)):
        total += nums[r]

        while (nums[r] * (r - left + 1)) - total > k:
            total -= nums[left]
            left += 1

        res = max(res, r - left + 1)

    return res


class Solution(object):
    pass
