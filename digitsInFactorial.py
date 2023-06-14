
import math 
class Solution:
    def digitsInFactorial(self,N):
        if N<0:
            return 0
        if N<=1:
            return 1
        x=(N*math.log10(N/math.e)+math.log10(2*math.pi*N)/2.0)
        return math.floor(x)+1
            
        
        
