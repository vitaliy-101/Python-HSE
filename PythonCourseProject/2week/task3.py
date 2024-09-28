# https://leetcode.com/problems/sort-vowels-in-a-string/submissions/1404730735/
from collections import deque


class Solution(object):
    def sortVowels(self, s):
        vowels = "AEIOUaeiou"
        q = deque(sorted(i for i in s if i in vowels))
        return "".join(q.popleft() if i in vowels else i for i in s)
