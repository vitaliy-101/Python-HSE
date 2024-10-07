# https://leetcode.com/problems/sort-the-students-by-their-kth-score/submissions/1414564207/
from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key=lambda i: -i[k])
