class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            
            # even
            l, r = i, i + 1
            while 0 <= l < r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
                
            # odd
            l, r = i, i
            while 0 <= l <= r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res