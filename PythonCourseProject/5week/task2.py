# https://leetcode.com/problems/optimal-partition-of-string/
class Solution:
    def partitionString(self, s: str) -> int:
        map = set()
        result = 1
        for st in s:
            if st in map:
                result += 1
                map = set()
                map.add(st)
                continue
            map.add(st)
        return result
