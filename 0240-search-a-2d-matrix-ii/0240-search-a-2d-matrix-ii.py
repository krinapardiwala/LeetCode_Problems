class Solution(object):
    def searchMatrix(self, matrix, target):
        rows=len(matrix)
        cols=len(matrix[0])
        row=0
        col=cols-1  

        while row<rows and col>=0:   #starts with top right corner element
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                col-=1   #moves left in the same row
            else:
                row+=1  #if element is smaller, change the row.
        return False