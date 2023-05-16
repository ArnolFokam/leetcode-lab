from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        pair = sorted(pair, lambda x: x[0])[::-1]
        
        stack = []
        
        for p, s in pair:
            # what time will it take to reach the target
            stack.append((target - p) / s)
            
            if len(stack) > 2 and stack[-1] <= stack[-2]:
                # they collide
                stack.pop()
                
        return len(stack)
        
        