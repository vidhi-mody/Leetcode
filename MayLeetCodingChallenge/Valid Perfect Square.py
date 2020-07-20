"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Example 1:

Input: num = 16
Output: true

Example 2:

Input: num = 14
Output: false

Constraints:
1 <= num <= 2^31 - 1
"""
def isSquare(start,end,num):
    while(start<=end):
        mid = start + (end-start)//2
        if(mid*mid==num):
            return True
        elif(mid*mid > num):
            end = mid - 1
        else:
            start = k=mid + 1
    return False
        

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if(num<=1):
            return True
        else:
            ans = isSquare(2,num,num)
            return ans
