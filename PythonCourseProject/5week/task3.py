# https://leetcode.com/problems/find-all-duplicates-in-an-array/
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = {}
        duplicates = []

        for index, value in enumerate(nums):
            if value in dic:
                duplicates.append(value)
            else:
                dic[value] = 1

        return duplicates
