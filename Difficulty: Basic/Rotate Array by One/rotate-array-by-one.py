#User function Template for python3

class Solution:
    def rotate(self, arr):
        a= arr.pop()
        arr.insert(0,a)
        return arr
