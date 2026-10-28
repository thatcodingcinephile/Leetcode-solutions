class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        row,col=0,n-1
        while row<m and col>=0:
            current=matrix[row][col]
            if current==target:
                return True
            elif current>target:
                col-=1
            else:
                row+=1
        return False