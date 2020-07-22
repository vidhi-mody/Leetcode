"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        answer = [0] * (num + 1)
        
        for pow in range(0, 32):
            begin = 1<<pow
            end = 1<<(pow + 1)
            if(begin > num):
                break
            for i in range(begin, min(num+1,end)):
                answer[i] = answer[i-begin] + 1
                
        return answer 
