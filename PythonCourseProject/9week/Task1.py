from idlelib.tree import TreeNode
from typing import List, Optional


# https://leetcode.com/problems/unique-binary-search-trees-ii/submissions/1484552856/?envType=problem-list-v2&envId=binary-tree


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        memo = {}

        def generate_trees(start, end):
            if (start, end) in memo:
                return memo[(start, end)]

            trees = []
            if start > end:
                trees.append(None)
                return trees

            for root_val in range(start, end + 1):
                left_trees = generate_trees(start, root_val - 1)
                right_trees = generate_trees(root_val + 1, end)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(root_val, left_tree, right_tree)
                        trees.append(root)

            memo[(start, end)] = trees
            return trees

        return generate_trees(1, n)
