"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
def findDist(word1, word2, len1, len2): 

    minDist = [[0 for x in range(len2 + 1)] for x in range(len1 + 1)] 

    for i in range(len1 + 1): 
        for j in range(len2 + 1): 
            if i == 0: 
                minDist[i][j] = j
                
            elif j == 0: 
                minDist[i][j] = i
                
            elif word1[i-1] == word2[j-1]: 
                minDist[i][j] = minDist[i-1][j-1] 
  
            else: 
                minDist[i][j] = 1 + min(minDist[i][j-1], minDist[i-1][j], minDist[i-1][j-1])
  
    return minDist[len1][len2] 

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        answer = findDist(word1, word2, len(word1), len(word2))
        return answer
