class Solution(object):
    def searchMatrix(self, matrix, target):
        rows=len(matrix)
        cols=len(matrix[0])

        start=0
        end=(rows*cols)-1   #-1 as indexing starts from 0

        while start<=end:
            mid=(start+end)//2
            row=mid//cols  #this is because mid represents the index and its floor division with cols gives the row in which the index is. row starts after: no.of previous rows*no.of columns.
            col=mid%cols

            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                start=mid+1  #move start towards right
            else:
                end=mid-1  #move end towards the left
        return False
        
        #linear search approach
        '''rows=len(matrix)
        cols=len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==target:
                    return True
        return False'''
        