class Solution:
    def findEquilibrium(self, arr):
        n = len(arr)
        prefix = [0]*(n+1)
        
        for i in range(1,n+1):
            prefix[i] = prefix[i-1] + arr[i-1]
        
        
        for i in range(1,n+1):
            if prefix[i-1] == prefix[n]-prefix[i]:
                return i - 1
        return -1

