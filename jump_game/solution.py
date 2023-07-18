from typing import List

# dynamic programming
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums[-1] = True

        for i in range(len(nums) - 2, -1, -1):

            can_reach_last = False
            
            for j in range(i + 1, min(len(nums), i + nums[i] + 1)):
                
                if nums[j] == True:
                    can_reach_last = True
                    break
            
            nums[i] = can_reach_last

        return nums[0]
    
# greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal_position = len(nums) -  1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal_position:
                goal_position = i

        return goal_position == 0