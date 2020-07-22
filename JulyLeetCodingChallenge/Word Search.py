"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 
Constraints:
board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def backtrack(i, j, idx):
            char = board[i][j]
            if(char != word[idx]):
                return False
            elif(idx == len(word)-1):
                return True
            
            board[i][j] = ''
            
            if(i > 0 and backtrack(i-1, j, idx+1)):
                return True
            if(j > 0 and backtrack(i, j-1, idx+1)):
                return True
            if(i < rows-1 and backtrack(i+1, j, idx+1)):
                return True
            if(j < cols-1 and backtrack(i, j+1, idx+1)):
                return True            
            board[i][j] = char
            return False
                    
        for i in range(rows):
            for j in range(cols):
                if(backtrack(i, j, 0)):
                    return True
            
        return False