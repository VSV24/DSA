class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashed = set()
        for i in range(len(nums)):
            if nums[i] in hashed:
                return True
            hashed.add(nums[i])
        return False
        