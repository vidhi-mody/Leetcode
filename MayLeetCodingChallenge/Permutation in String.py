"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Hash=0
        s2Hash=0
        
        if len(s2)<len(s1):
            return False
        
        for i in s1:
            s1Hash+=hash(i)
        for i in range(len(s1)):
            s2Hash+=hash(s2[i])

        if s1Hash==s2Hash:
            return True
        
        if len(s2)>len(s1):
            for j in range(len(s1),len(s2)):
                s2Hash+=hash(s2[j])-hash(s2[j-len(s1)])
                if s1Hash==s2Hash:
                    return True
                
        return False
