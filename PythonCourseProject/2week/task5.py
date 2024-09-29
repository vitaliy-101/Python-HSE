# https://leetcode.com/problems/partition-labels/
class Solution(object):
    def partitionLabels(self, s):
        alf = [0 for i in range(26)]
        for i in range(len(s)):
            alf[ord(s[i]) - 97] = max(alf[ord(s[i]) - 97], i)
        localMax = 0
        localResult = 0
        result = []
        for i in range(len(s)):
            localMax = max(localMax, alf[ord(s[i]) - 97])
            localResult += 1
            if i == localMax:
                result.append(localResult)
                localResult = 0
        return result
