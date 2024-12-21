# https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/1484559784/?envType=problem-list-v2&envId=binary-tree
from idlelib.tree import TreeNode
from typing import Optional


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            self.result.append(node.val)
            inorder(node.right)

        inorder(root)
        return self.result[k - 1]
