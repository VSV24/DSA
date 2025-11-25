class Solution:
	def pushZerosToEnd(self, arr):
    	n = len(arr)
    	count = 0
    	for i in range(n):
    	    if arr[i]!=0:
    	        arr[count],arr[i] = arr[i],arr[count]
    	        count+=1
    	       
    	
    	
    	