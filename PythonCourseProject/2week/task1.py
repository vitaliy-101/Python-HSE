# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/submissions/1404716244/
class Solution(object):
    def numberOfBeams(self, bank):
        if len(bank) <= 1:
            return 0
        lastCount = bank[0].count("1")
        result = 0
        for i in range(1, len(bank)):
            nowCount = bank[i].count("1")
            result += nowCount * lastCount
            if nowCount != 0:
                lastCount = nowCount
        return result
