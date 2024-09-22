# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution(object):

    def getResult(self, digits, index, current, result, data):
        if index == len(digits):
            result.append(current)
            return
        for letter in data[digits[index]]:
            self.getResult(digits, index + 1, current + letter, result, data)

    def letterCombinations(self, digits):
        result = []
        data = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.getResult(digits, 0, "", result, data)
        if result == [""]:
            return []
        return result
