# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/submissions/1455642984/?envType=problem-list-v2&envId=sliding-window
class Solution:
    def minimumCardPickup(self, cards):
        n = len(cards)
        card_map = {}
        min_length = n + 1

        for j in range(n):
            if cards[j] in card_map:
                min_length = min(min_length, j - card_map[cards[j]] + 1)
            card_map[cards[j]] = j

        return min_length if min_length <= n else -1
