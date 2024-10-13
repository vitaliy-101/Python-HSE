# https://leetcode.com/problems/max-increase-to-keep-city-skyline/submissions/1421377982/
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        N = len(grid)
        M = len(grid[0])

        grid_t = zip(*grid)

        sk_v = [max(row) for row in grid]
        sk_h = [max(row) for row in grid_t]

        res = 0
        for i in range(N):
            for j in range(M):
                diff = min(sk_h[j], sk_v[i]) - grid[i][j]
                res += diff
        return res
