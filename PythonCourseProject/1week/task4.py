# https://leetcode.com/problems/sort-characters-by-frequency/submissions/1398447321/
class Solution(object):
    def frequencySort(self, s):
        frequency_number = [0 for i in range(130)]
        for element in s:
            frequency_number[ord(element)] += 1
        frequency_number_zip = list(zip(frequency_number, [i for i in range(130)]))
        frequency_number_zip.sort(key=lambda x: x[0])
        result = ""
        for element in frequency_number_zip[-1::-1]:
            result += element[0] * chr(element[1])
        return result
