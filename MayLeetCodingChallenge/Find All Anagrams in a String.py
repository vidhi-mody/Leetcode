"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s1Hash=0
        s2Hash=0
        answer=[]
        
        if len(s)<len(p):
            return answer
        
        for i in range(len(p)):
            s1Hash+=hash(s[i])
        for i in range(len(p)):
            s2Hash+=hash(p[i])
            
        if s1Hash==s2Hash:
            answer.append(0)
        
        if len(s)>len(p):
            i=1
            for j in range(len(p),len(s)): 
                s1Hash+=hash(s[j])-hash(s[j-len(p)])
                if s1Hash==s2Hash:
                    answer.append(i)
                i=i+1
                
        return answer
