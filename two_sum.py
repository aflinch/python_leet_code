# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def two_sum(self, nums, target):
        visited = {}
        
        for i, num in enumerate(nums):
            inverse_target = target - num
            
            if inverse_target in visited:
                return [visited[inverse_target], i]
            
            visited[num] = i
            
        return None

print(Solution().two_sum([2, 7, 11, 15], 9))