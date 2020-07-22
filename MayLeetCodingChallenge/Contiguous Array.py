"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
"""
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)<=1):
            return 0
        count=0
        maxLength=0
        counter={0:-1}
        for index, value in enumerate(nums): 
            
            if(value==1):
                count = count + 1
            
            else:
                count = count - 1
           
            if count in counter:
                maxLength=max(maxLength,index-counter[count])
                
            else:
                counter[count]=index
        
        return maxLength
        
