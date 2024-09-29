# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/submissions/1405985897/
class Solution(object):
    def minSteps(self, s, t):
        alf = [0 for i in range(26)]
        for el in s:
            alf[ord(el) - 97] += 1
        for el in t:
            if alf[ord(el) - 97] == 0:
                continue
            alf[ord(el) - 97] -= 1
        return sum(alf)
