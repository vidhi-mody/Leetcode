"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        x = "{0:b}".format(x)
        y = "{0:b}".format(y)
        if(len(x) > len(y)):
            y = "0"*(len(x) - len(y)) + y
        else:
            x = "0"*(len(y) - len(x)) + x
        print(x)
        print(y)
        for i in range(0,len(x)):
            if(x[i]!=y[i]):
                count = count + 1
        return count
