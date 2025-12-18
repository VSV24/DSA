class Solution:
    def closestNumber(self, n, m):
        q = int(n/m)
        
        n1 = m*q
        
        if ((n*m)>0):
            n2 = (m*(q+1))
        else:
            n2 = (m*(q-1))
        
        d1 = abs(n-n1)
        d2 = abs(n-n2)
        
        if d1 > d2:
            return n2
        elif d2 > d1:
            return n1
        else:
            return n1 if abs(n1)>abs(n2) else n2