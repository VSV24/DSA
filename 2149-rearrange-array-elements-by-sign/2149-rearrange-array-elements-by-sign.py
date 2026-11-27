class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0]*n
        pos,neg = 0,1

        for i in range(n):
            if nums[i] < 0:
                ans[neg] = nums[i]
                neg+=2
            else:
                ans[pos] = nums[i]
                pos+=2
        return ans
