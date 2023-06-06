class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        curL = 0

        for i in range(len(s)):
            
            # even
            l, r = i, i + 1
            while 0 <= l < r < len(s) and s[l] == s[r]:    
                if curL < r - l + 1:
                    curL = r - l + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1
                
            # odd
            l, r = i, i
            while 0 <= l <= r < len(s) and s[l] == s[r]:
                if curL < r - l + 1:
                    curL = r - l + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1

        return res