class Solution(object):
    def generate(self, numRows):
        l=[]
        for i in range(numRows):
            x=[1]
            

            if i>0:
                z=l[i-1]
                for j in range(1,i):
                    x.append(z[j-1]+z[j])
                
                x.append(1)
            l.append(x)
        return l

        
            
            


            




        
        
