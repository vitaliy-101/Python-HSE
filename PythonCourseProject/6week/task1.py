# https://leetcode.com/problems/minimum-size-subarray-sum/?envType=problem-list-v2&envId=sliding-window
class Solution(object):
    def minSubArrayLen(self, target, nums):
        l, r = 0, 1
        minLen = 1000000
        value = sum(nums[l:r])
        numSize = len(nums)
        while True:
            if value >= target:
                minLen = min(minLen, r - l)
                value -= nums[l]
                l += 1
                if l == r:
                    minLen = 1
                    break
            else:
                if r >= numSize:
                    break
                value += nums[r]
                r += 1
        if minLen == 1000000:
            return 0
        else:
            return minLen
