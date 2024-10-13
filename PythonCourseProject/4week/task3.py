# https://leetcode.com/problems/maximum-binary-tree/
from idlelib.tree import TreeNode
from typing import List, Optional


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def BFS(nums):
            if not nums:
                return None
            maxvalue, index = float("-inf"), -1
            for i in range(len(nums)):
                if nums[i] > maxvalue:
                    maxvalue = nums[i]
                    index = i
            root = TreeNode(maxvalue)
            root.left, root.right = BFS(nums[0:index]), BFS(nums[index + 1 :])
            return root

        return BFS(nums)
