# https://leetcode.com/problems/longest-nice-substring/submissions/1484541559/?envType=problem-list-v2&envId=sliding-window
class Solution:
    def longestNiceSubstring(self, s) -> str:
        if not (1 <= len(s) <= 100):
            return ""
        else:

            max_length = 0
            longest_nice_substring = ""

            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    substring = s[i:j]
                    if self.is_nice(substring):
                        if len(substring) > max_length:
                            max_length = len(substring)
                            longest_nice_substring = substring
            return longest_nice_substring

    def is_nice(self, substring):
        lowers = set()
        uppers = set()
        for letter in substring:
            if letter.islower():
                lowers.add(letter)
            else:
                uppers.add(letter)

        for lower_element in lowers:
            if lower_element.upper() not in uppers:
                return False
        if len(lowers) == len(uppers):
            return True
