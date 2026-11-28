class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        rowIndex = rowIndex + 1
        ans = 1
        ans_row = []
        ans_row.append(1)
        for col in range(1,rowIndex):
            ans = ans * (rowIndex - col)
            ans = ans // col
            ans_row.append(ans)
        return ans_row