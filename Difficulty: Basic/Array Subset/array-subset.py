#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        Map = {}
        if len(b) > len(a):
            return False
        for i in b:
            if i in Map:
                Map[i] += 1
            else:
                Map[i] = 1
        
        for i in a:
            if i in Map:
                Map[i] -= 1
        
        for i,value in Map.items():
            if value > 0:
                return False
        return True
            
    
    
    
