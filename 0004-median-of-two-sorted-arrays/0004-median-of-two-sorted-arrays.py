class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        com = nums1+nums2
        com.sort()
        n =len(com)
        mid = int(n/2)
        if n%2==0:
            return (com[mid-1]+com[mid])/2
        else:
            return com[mid]
