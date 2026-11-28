class Solution:
    def generate_row(row):
        ans = 1
        ans_row = []
        for col in range(1,row):
            ans = ans * (row - col)
            ans = ans // col
            ans_row.append(ans)
        return ans_row
    def generate(self, numRows: int) -> list[list[int]]:
        def generate_row(row):
            ans = 1
            ans_row = []
            ans_row.append(1)
            for col in range(1,row):
                ans = ans * (row - col)
                ans = ans // col
                ans_row.append(ans)
            return ans_row
        res = []
        for i in range(1,numRows+1):
            res.append(generate_row(i))
        return res
        