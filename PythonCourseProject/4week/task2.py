# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/submissions/1421378395/
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        ans = ans ^ k
        return bin(ans).count("1")
