'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        edge_lenght = len(matrix)
        
        top = 0
        bottom = edge_lenght - 1
        
        while top < bottom:
            for col in range(edge_lenght):
                temp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp
            top += 1
            bottom -= 1
        
        for row in range(edge_lenght):
            for col in range(row+1, edge_lenght):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
        
        return matrix