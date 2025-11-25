class Solution:
    def getSecondLargest(self, arr):
        n= len(arr)
        last = -1
        secondlast = -1
        
        for i in range(n):
            
            if arr[i]>last:
                secondlast = last
                last = arr[i]
                
                
            elif arr[i]<last and arr[i]>secondlast:
                secondlast = arr[i]
                
        return secondlast