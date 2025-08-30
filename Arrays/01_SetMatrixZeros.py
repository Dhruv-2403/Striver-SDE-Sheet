class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """ 

        # O(1) space complexity(Best Approach)
        # O(m*n) Time Complexity
        n=len(matrix)
        m=len(matrix[0])
        flag_row=False
        flag_col=False
        for i in matrix[0]:
            if i==0:
                flag_row=True
        for i in range(len(matrix)):
            if matrix[i][0]==0:
                flag_col=True


     

        for i in range(1,len(matrix[0])):
            for j in range(1,len(matrix)):


                if matrix[j][i]==0:
                    matrix[0][i]=0  
                    matrix[j][0]=0
        for i in range(1,len(matrix[0])):
            for j in range(1,len(matrix)):
                if matrix[0][i]==0 or matrix[j][0]==0:
                    matrix[j][i]=0
        if flag_row:
            for i in range(len(matrix[0])):
                matrix[0][i]=0

        
        if flag_col:
            for i in range(len(matrix)):
                matrix[i][0]=0
        return matrix



        #Brute Force Approach(O(Number of Zeros) Space Complexity)

        x=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    x.append((i,j))
                    
                else:
                    continue
        # return x

        for i in range(len(x)):
            a,b=x[i]

            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if i==a or j==b:
                        matrix[i][j]=0

