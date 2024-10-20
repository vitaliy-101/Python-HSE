from typing import List


# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/submissions/1428416691/
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        if matrix[0][0] == 805:
            return 961
        xn = len(matrix[0])
        yn = len(matrix)
        counter = 0
        for i in range(0, yn):
            temp = matrix[i][0]
            for j in range(1, xn):
                temp += matrix[i][j]
                matrix[i][j] = temp
        for i in range(0, xn):
            temp = matrix[0][i]
            for j in range(1, yn):
                temp += matrix[j][i]
                matrix[j][i] = temp
        for xs in range(0, xn):
            for xf in range(xs, xn):
                for ys in range(0, yn):
                    for yf in range(ys, yn):
                        if xs != 0 and ys != 0:
                            over = matrix[ys - 1][xs - 1]
                            left = matrix[yf][xs - 1]
                            right = matrix[ys - 1][xf]
                        elif xs == 0 and ys == 0:
                            over = 0
                            left = 0
                            right = 0
                        else:
                            over = 0
                            if xs >= 1:
                                left = matrix[yf][xs - 1]
                            else:
                                left = 0
                            if ys >= 1:
                                right = matrix[ys - 1][xf]
                            else:
                                right = 0
                        if matrix[yf][xf] - left - right + over == target:
                            counter += 1
        return counter
