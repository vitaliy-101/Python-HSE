from idlelib.tree import TreeNode
from typing import Optional


# https://leetcode.com/problems/recover-binary-search-tree/submissions/1484553509/?envType=problem-list-v2&envId=binary-tree
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        traverse_lst = []
        violated_pairs = []
        prev = None

        def get_violated_pairs():
            node1, node2 = None, None
            if len(violated_pairs) == 1:
                node1, node2 = violated_pairs[0]  # case 1
            else:
                node1, node2 = violated_pairs[0][0], violated_pairs[1][1]  # case 2

            return node1, node2

        def inorder(node):
            nonlocal prev
            if node:
                inorder(node.left)
                if prev and node.val < prev.val:
                    violated_pairs.append((prev, node))
                traverse_lst.append(node.val)
                prev = node
                inorder(node.right)

        inorder(root)
        a, b = get_violated_pairs()

        # swap values
        a.val, b.val = b.val, a.val
