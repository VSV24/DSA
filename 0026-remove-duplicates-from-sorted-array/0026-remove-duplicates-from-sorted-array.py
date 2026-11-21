class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        first = 0
        for second in range(1,n):
            if nums[first] != nums[second]:
                first += 1
                nums[first],nums[second] = nums[second],nums[first]
        return first+1