class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        temp = []
        n = len(nums)
        steps = k % n
        x,y = n-steps,0
        for _ in range(n):
            if x < n:
                temp.append(nums[x])
                x+=1
            elif y < n-steps:
                temp.append(nums[y])
                y+=1
        nums[:] = temp
        


