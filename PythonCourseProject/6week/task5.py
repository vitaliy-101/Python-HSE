# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/?envType=problem-list-v2&envId=sliding-window
from cmath import inf, isinf
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        a = 0
        orWindow = 0
        setBitCount = [0 for i in range(31)]
        answer = inf

        for b in range(n):
            orWindow |= nums[b]

            bitNum = nums[b]
            i = 0
            while bitNum > 0:
                if bitNum & 1:
                    setBitCount[i] += 1
                bitNum >>= 1
                i += 1

            while a <= b and orWindow >= k:
                answer = min(answer, b - a + 1)
                bitNum = nums[a]
                i = 0
                while bitNum > 0:
                    if bitNum & 1:
                        setBitCount[i] -= 1
                        if not setBitCount[i]:
                            orWindow -= 2**i
                    bitNum >>= 1
                    i += 1
                a += 1

        return -1 if isinf(answer) else answer
