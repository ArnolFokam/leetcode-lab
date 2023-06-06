class Solution:
    def climbStairs(self, n: int) -> int:
        before_last, last = 1, 1
        
        for _ in range(2, n + 1):
            before_last, last = before_last + last, before_last
            
        return before_last
