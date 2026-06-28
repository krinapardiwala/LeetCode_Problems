class Solution(object):
    def findPeakGrid(self, mat):
        res=[] #empty result list
        row=len(mat)-1  #no.of rows in the matrix.minus 1 done to cater the last row as well.
        top=0  #extreme top. 

        while row>top:
            mid=(top+row)//2  #binary search
            if max(mat[mid])>max(mat[mid+1]): #if maximum element is in mat[mid], then it is for sure that row below it has min element. thus, row equals mid then.
                row=mid
            else:
                top=mid+1 #top goes to the next one.
        res.append(row)
        res.append(mat[row].index(max(mat[row])))
        return res
        
        
        