"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (not grid[i][j]): 
                    continue
                if (i == 0 or not grid[i-1][j]): 
                    perimeter = perimeter + 1
                if (i >= len(grid)-1 or not grid[i+1][j]): 
                    perimeter = perimeter + 1
                if (j == 0 or not grid[i][j-1]): 
                    perimeter = perimeter + 1
                if (j >= len(grid[0])-1 or not grid[i][j+1]): 
                    perimeter = perimeter + 1
        return perimeter
        
