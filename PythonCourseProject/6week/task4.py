# https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/submissions/1455643670/?envType=problem-list-v2&envId=sliding-window
from cmath import inf
from typing import List


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        N = len(nums)
        min_len = float(inf)
        total = sum(nums)
        extra, target = divmod(target, total)
        target = total - target
        left = 0
        running_sum = 0
        for right in range(2 * N):
            running_sum += nums[right % N]
            while running_sum > target:
                running_sum -= nums[left % N]
                left += 1
            if running_sum == target:
                min_len = min(min_len, N - (right - left + 1))
        if min_len == float(inf):
            return -1
        return extra * N + min_len
