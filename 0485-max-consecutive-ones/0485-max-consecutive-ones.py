class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        high = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
            else:
                high = max(count,high)
                count = 0
        if count > high:
            high = count
        return high
