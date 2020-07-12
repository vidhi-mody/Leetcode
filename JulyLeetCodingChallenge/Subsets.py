"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]] 
        n = len(nums)
        
        for i in range(2**n): 
            subset = []
            for j in range(n): 
                if (i & (1 << j)) != 0: 
                    subset.append(nums[j])
            if subset not in answer and len(subset) > 0: 
                answer.append(subset)
                
        return(answer)