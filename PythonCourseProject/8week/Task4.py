from typing import List


# https://leetcode.com/problems/k-radius-subarray-averages/submissions/1484549198/?envType=problem-list-v2&envId=sliding-window
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)
        li = k * 2 + 1
        sum = 0

        for i in range(0, li):
            if i >= n:
                break
            sum += nums[i]

        for i in range(n):
            if i - k >= 0 and i + k < n:
                ans.append(int(sum / li))
                sum -= nums[i - k]
                if i + k + 1 < n:
                    sum += nums[i + k + 1]
            else:
                ans.append(-1)

        return ans
