from collections import deque
from idlelib.tree import TreeNode
from typing import List, Optional


# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/1484553934/?envType=problem-list-v2&envId=binary-tree


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        level = 0
        ans = []
        queue = deque()
        queue.append(root)

        # print(queue)

        while queue:
            curr_len = len(queue)
            curr_queue = deque()

            for i in range(curr_len):
                curr = queue.popleft()
                # print(curr)
                if level % 2 == 0:
                    curr_queue.append(curr.val)
                else:
                    curr_queue.appendleft(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            ans.append(list(curr_queue))
            level += 1

            # print(ans)

        return ans
