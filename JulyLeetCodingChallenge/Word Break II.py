"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        letters = set(s)
        complete_strng = set(''.join(wordDict))
        if not all(char in complete_strng for char in letters):
            return []
        ans = []
        queue = deque([[word, s, [word]] for word in wordDict if s.startswith(word)])
        while queue:
            word, new_s, lista = queue.popleft()
            if new_s.startswith(word):
                new_s = new_s.replace(word, '', 1)
            if new_s == '':
                ans.append(' '.join(lista))
            for word in wordDict:
                if new_s.startswith(word):
                    queue.append([word, new_s, lista + [word]])
        return ans