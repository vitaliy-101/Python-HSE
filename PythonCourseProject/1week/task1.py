#https://leetcode.com/problems/simplified-fractions/?envType=problem-list-v2&envId=string&difficulty=MEDIUM%2CHARD&status=SOLVED


class Solution(object):
    def gcd(self, a, b):
        while b != 0:
            c = b
            b = a % b
            a = c
        return a

    def simplifiedFractions(self, n):
        itog = []
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                if self.gcd(i, j) == 1:
                    itog.append(str(i) + "/" + str(j))
        return itog
