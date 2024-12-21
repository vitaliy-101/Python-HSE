# https://leetcode.com/problems/jump-game-vii/submissions/1484547221/?envType=problem-list-v2&envId=sliding-window
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False
        legal_jumps = [False] * (len(s) + 1)
        legal_jumps[0], prefix_sum = True, 0
        for i in range(minJump, len(s)):
            prefix_sum += legal_jumps[i - minJump if i - minJump >= 0 else -1]
            if prefix_sum and s[i] == "0":
                legal_jumps[i] = True
            prefix_sum -= legal_jumps[i - maxJump if i - maxJump >= 0 else -1]
        return legal_jumps[-2]
