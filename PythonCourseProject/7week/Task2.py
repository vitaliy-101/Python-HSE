from typing import List


# https://leetcode.com/problems/maximum-erasure-value/submissions/1484541160/?envType=problem-list-v2&envId=sliding-window


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = set()
        left = 0
        max_sum = 0
        cur_sum = 0

        for right, num in enumerate(nums):
            # check the element that pointed by 'left'
            while num in s:
                s.remove(nums[left])
                cur_sum -= nums[left]
                left += 1

            cur_sum += num
            s.add(num)
            max_sum = max(max_sum, cur_sum)

        return max_sum
