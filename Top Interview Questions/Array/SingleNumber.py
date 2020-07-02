"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0,len(nums),2):
            if(i==len(nums)-1):
                return nums[i]
            elif(nums[i]!=nums[i+1]):
                return nums[i]
