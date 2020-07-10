"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            
            if( i > 0 and nums[i] == nums[i - 1]):
                continue
                
            while( j < k ):
                if(k < len(nums) - 1 and nums[k] == nums[k + 1]):
                    k = k - 1
                    continue
                if (nums[i] + nums[j] + nums[k] > 0):
                    k = k -1
                elif(nums[i] + nums[j] + nums[k] < 0):
                    j = j + 1
                else:
                    triplet = []
                    triplet.append(nums[i])
                    triplet.append(nums[j])
                    triplet.append(nums[k])
                    answer.append(triplet)
                    j = j + 1
                    k = k - 1
        
        return answer
