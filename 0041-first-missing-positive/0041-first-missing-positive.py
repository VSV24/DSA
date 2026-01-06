class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num > 0:
                seen.add(num)

        i = 1
        while i in seen:
            i += 1

        return i