class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1],[1,1]]
        for i in range(2,rowIndex+1):
            res.append([1]*(i+1))
            for j in range(1,i):
                res[i][j] = res[i-1][j] + res[i-1][j-1]
        return res[rowIndex]
