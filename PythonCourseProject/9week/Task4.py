# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/submissions/1484554384/?envType=problem-list-v2&envId=binary-tree
from idlelib.tree import TreeNode
from typing import List, Optional


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder.pop())
        mid = inorder.index(root.val)
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1 :], postorder[mid:])
        return root
