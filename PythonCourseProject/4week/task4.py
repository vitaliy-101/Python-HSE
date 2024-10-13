# https://leetcode.com/problems/sort-the-matrix-diagonally/submissions/1421380037/
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = {}
        li = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if row - col in d:
                    d[row - col] = d[row - col] + [mat[row][col]]
                else:
                    d[row - col] = [mat[row][col]]
        for i in d:
            d[i] = sorted(d[i])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if len(d[i - j]) > 1:
                    li.append(d[i - j][0])
                    d[i - j] = d[i - j][1:]
                else:
                    li.append(d[i - j][0])
        k = []
        while li != []:
            k.append(li[: len(mat[0])])
            li = li[len(mat[0]) :]
        return k
