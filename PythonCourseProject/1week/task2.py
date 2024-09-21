# https://leetcode.com/problems/multiply-strings/?envType=problem-list-v2&envId=string&difficulty=MEDIUM%2CHARD
class Solution(object):
    def multiply_numbers(self, num1, num2):
        len1, len2 = len(num1), len(num2)
        result = [0] * (len1 + len2)
        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                now_number = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                index1 = i + j
                index2 = i + j + 1
                sum = now_number + result[index2]
                result[index2] = sum % 10
                result[index1] += sum // 10
        result_number = "".join(map(str, result))
        return result_number.lstrip("0")

    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        return self.multiply_numbers(num1, num2)
