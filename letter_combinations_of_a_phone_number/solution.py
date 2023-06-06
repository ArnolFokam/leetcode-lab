from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digitsTochar = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        subset = []

        def dfs(i):
            if i >= len(digits):
                if len(subset) > 0:
                    res.append("".join(subset.copy()))

            else:
                for c in digitsTochar[digits[i]]:
                    subset.append(c)
                    dfs(i + 1)
                    subset.pop()


        dfs(0)

        return res