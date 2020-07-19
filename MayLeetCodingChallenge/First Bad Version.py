"""
ou are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def findBadVersion(start,end):
    mid=(start+end)//2
    first=start
    if(isBadVersion(first)==True):
        return start
    elif(isBadVersion(mid)==True and isBadVersion(mid-1)==False):
        return(mid)
    elif(isBadVersion(mid)==False):
        return findBadVersion(mid+1,end)
    else:
        return findBadVersion(start,mid-1)
    

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        answer=findBadVersion(1,n)
        return answer