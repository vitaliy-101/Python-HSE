#https://leetcode.com/problems/custom-sort-string/submissions/1397227628/
class Solution(object):
    def customSortString(self, order, s):
        s_used_characters = [0 for el in range(26)]
        result = ''
        for el in s:
            s_used_characters[ord(el) - 97] += 1
        for el in order:
            result += el * s_used_characters[ord(el) - 97]
            s_used_characters[ord(el) - 97] = 0
        for number in range(26):
            result += chr(number + 97) * s_used_characters[number]
        return result
