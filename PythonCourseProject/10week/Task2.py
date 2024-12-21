# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/submissions/1484558213/?envType=problem-list-v2&envId=binary-tree
from collections import deque
from lib2to3.pytree import Node


class Solution:
    def connect(self, root: "Node") -> "Node":
        q = deque([root])

        while q:
            n = len(q)
            prev = None

            for _ in range(n):
                node = q.popleft()

                if node:
                    if prev:
                        prev.next = node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

                prev = node

        return root
