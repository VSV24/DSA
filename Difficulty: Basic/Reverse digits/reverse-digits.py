#User function Template for python3

class Solution:
	def reverseDigits(self, n):
    	r = 0
        if n == 0:
            return n
        while n != 0:
            poped = n%10
            r = (r*10) + poped
            n //=10
        return r