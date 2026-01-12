class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {}
        for i,l in enumerate(order):
            orderMap[l] = i
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    curr = orderMap[words[i][j]]
                    nex = orderMap[words[i+1][j]]
                    if nex < curr:
                        return False
                    else:
                        break
        return True