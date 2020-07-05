"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
"""

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        answer = [1]
        u2 = u3 = u5 = 0
        count = 0
        
        while n > 1:
            val = min(answer[u2]*2, answer[u3]*3,answer[u5]*5)
            if val == answer[u2]*2:
                u2 = u2 + 1
            if val == answer[u3]*3:
                u3 = u3 + 1
            if val == answer[u5]*5:
                u5 = u5 + 1
            n = n - 1
            answer.append(val)
            
        return answer[-1]
