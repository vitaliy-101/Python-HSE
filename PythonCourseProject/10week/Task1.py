# https://leetcode.com/problems/path-sum-ii/?envType=problem-list-v2&envId=binary-tree
from idlelib.tree import TreeNode
from typing import List


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(root, targetSum, path):
            if root is None:
                return None
            targetSum -= root.val
            path.append(root.val)
            if root.left is None and root.right is None:  # Is leaf node
                if targetSum == 0:  # Found a valid path
                    ans.append(path.copy())
            else:
                dfs(root.left, targetSum, path)
                dfs(root.right, targetSum, path)
            path.pop()  # backtrack

        ans = []
        dfs(root, targetSum, [])
        return ans
