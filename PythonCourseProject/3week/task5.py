from typing import List


# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/submissions/1414566733/
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        return [len(set(A[: i + 1]) & set(B[: i + 1])) for i in range(len(A))]
