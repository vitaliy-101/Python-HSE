from collections import defaultdict


# https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/submissions/1484546180/?envType=problem-list-v2&envId=sliding-window
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        d = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        res = 0
        stack = []
        newd = defaultdict(int)
        for r in range(len(word)):
            if not stack:
                stack.append(word[r])
                newd[word[r]] += 1
                continue
            if stack and d[word[r]] >= d[stack[-1]]:
                stack.append(word[r])
                newd[word[r]] += 1
                if newd["a"] and newd["e"] and newd["i"] and newd["o"] and newd["u"]:
                    res = max(res, len(stack))
            else:
                stack.clear()
                newd.clear()
                stack.append(word[r])
                newd[word[r]] += 1
        return res
