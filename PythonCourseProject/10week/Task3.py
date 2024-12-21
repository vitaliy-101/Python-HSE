# https://leetcode.com/problems/sum-root-to-leaf-numbers/submissions/1484558757/?envType=problem-list-v2&envId=binary-tree
from idlelib.tree import TreeNode
from typing import Optional


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path_sum):
            if not node:
                return 0
            path_sum = path_sum * 10 + node.val
            if not node.left and not node.right:
                return path_sum
            return dfs(node.left, path_sum) + dfs(node.right, path_sum)

        return dfs(root, 0)
