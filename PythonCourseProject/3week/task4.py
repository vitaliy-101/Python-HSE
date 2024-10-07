# https://leetcode.com/problems/reveal-cards-in-increasing-order/submissions/1414566126/
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = [0 for i in range(len(deck))]
        k = 1
        c = 0
        ans[0] = deck[0]

        while k < len(deck):
            for i in range(1, len(deck)):
                if ans[i] == 0:
                    c = c + 1
                    if c == 2:
                        ans[i] = deck[k]
                        k = k + 1
                        c = 0
        return ans
