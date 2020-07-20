"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
Check if these points make a straight line in the XY plane.

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:
2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if(len(coordinates)==2):
            return True
        else:
            a = coordinates[1][1] - coordinates[0][1] 
            b = coordinates[0][0] - coordinates[1][0]  
            c = a*(coordinates[0][0]) + b*(coordinates[0][1]) 
            for i in range(2,len(coordinates)):
                    if((a*coordinates[i][0] + b*coordinates[i][1])!=c):
                        return False   
            return True
