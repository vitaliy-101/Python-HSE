# https://leetcode.com/problems/partition-array-according-to-given-pivot/submissions/1411599134/
class Solution(object):
    def pivotArray(self, nums, pivot):
        result = []
        for i in nums:
            if i < pivot:
                result.append(i)
        for i in nums:
            if i == pivot:
                result.append(i)
        for i in nums:
            if i > pivot:
                result.append(i)
        return result
