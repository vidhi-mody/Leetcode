"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 

Note: You may assume the string contains only lowercase English letters.
"""
def first_non_repeating_character(str1):
  unique_char = []
  counter = {}
  for c in str1:
    if c in counter:
      counter[c] += 1
    else:
      counter[c] = 1 
      unique_char.append(c)
  for c in unique_char:
    if counter[c] == 1:
      return str1.index(c)
  return -1

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = first_non_repeating_character(s)
        return index
