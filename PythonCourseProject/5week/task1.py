from typing import List


# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/
class Solution:
    def convertNumber(self, number: int) -> int:
        st = str(number)[-1::-1]
        if st != "0":
            while st[0] == "0":
                st = st.replace("0", "", 1)
        return int(st)

    def countDistinctIntegers(self, nums: List[int]) -> int:
        result = set()
        for element in nums:
            result.add(element)
            result.add(self.convertNumber(element))
        return len(result)
