from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)

        breaks = set([-1])

        for i in range(len(s)):

            for b in breaks:
                if s[b + 1:i + 1] in wordDict:
                    breaks.add(i)
                    break

        return len(s) - 1 in breaks