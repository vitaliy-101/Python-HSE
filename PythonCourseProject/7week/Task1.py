# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1484540347/?envType=problem-list-v2&envId=sliding-window
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        def track(str_data):
            out = ""
            for i in str_data:
                if i not in out:
                    out += i
                else:
                    break
            return len(out)

        max_val = 0
        for i in range(len(s)):
            max_val = max(max_val, track(s[i:]))
        return max_val
