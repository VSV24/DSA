class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total = (n*(n+1))//2
        T = 0
        for i in range(n):
            T+=nums[i]

        missing = total - T

        return missing