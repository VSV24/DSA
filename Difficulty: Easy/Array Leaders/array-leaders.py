class Solution:
    def leaders(self, arr):
        res = []
        n = len(arr)
        max_right = arr[-1]
        res.append(max_right)
        
        for i in range(n-2,-1,-1):
            if arr[i] >= max_right:
                max_right = arr[i]
                res.append(max_right)
        res.reverse()
        return res