# https://leetcode.com/problems/binary-search-tree-iterator/submissions/1484559219/?envType=problem-list-v2&envId=binary-tree
from idlelib.tree import TreeNode
from typing import Optional


class BSTIterator:

    def inOrderTraversal(self, root, queue):
        if root is None:
            return
        self.inOrderTraversal(root.left, queue)
        queue.append(root.val)
        self.inOrderTraversal(root.right, queue)

    def __init__(self, root: Optional[TreeNode]):
        self.queue = []
        self.inOrderTraversal(root, self.queue)

    def next(self) -> int:
        return self.queue.pop(0)

    def hasNext(self) -> bool:
        return self.queue != []
