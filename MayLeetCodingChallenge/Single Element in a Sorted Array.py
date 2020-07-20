"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 
Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
"""
def findDuplicate(start,end,nums):  
    
    if(start==end):
        return(nums[end])
    
    mid = start + (end-start)//2

    if(mid%2==0):
        if(nums[mid]==nums[mid+1]):
            return findDuplicate(mid+2,end,nums)
        else:
            return findDuplicate(start,mid,nums)
    else:
        if(nums[mid] == nums[mid-1]): 
            return findDuplicate(mid+1, end, nums) 
        else: 
            return findDuplicate(start, mid-1, nums) 
                
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        answer = findDuplicate(0,len(nums)-1,nums)
        return answer
