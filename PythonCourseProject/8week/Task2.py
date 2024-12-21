# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/submissions/1484548216/?envType=problem-list-v2&envId=sliding-window
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s += s
        s1 = "01" * n
        s2 = "10" * n
        i = 0
        d = 100000
        c1 = 0
        c2 = 0
        c = 0
        for j in range(len(s)):
            if s[j] != s1[j]:
                c1 += 1
            if s[j] != s2[j]:
                c2 += 1
            if j - i + 1 == n:
                c = min(c1, c2)
                d = min(d, c)
                if s[i] != s1[i]:
                    c1 -= 1
                if s[i] != s2[i]:
                    c2 -= 1
                i += 1
        return d
