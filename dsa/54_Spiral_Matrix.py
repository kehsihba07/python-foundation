class Solution(object):
    def spiralOrder(self, matrix):
        n=len(matrix)
        m=len(matrix[0])
        total=m*n
        r=[]
        c=0
        rowstart=0
        rowend=n-1
        colstart=0
        colend=m-1
        while c<total:
            for i in range(colstart,colend+1):
                r.append(matrix[rowstart][i])
                c+=1
            rowstart+=1
            if c==total:
                break
            
            for i in range(rowstart,rowend+1):
                r.append(matrix[i][colend])
                c+=1
            colend-=1
            if c==total:
                break
            
            for i in range(colend,colstart-1,-1):
                r.append(matrix[rowend][i])
                c+=1
            rowend-=1
            if c==total:
                break
            
            for i in range(rowend,rowstart-1,-1):
                r.append(matrix[i][colstart])
                c+=1
            colstart+=1
            if c==total:
                break
        return r
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        