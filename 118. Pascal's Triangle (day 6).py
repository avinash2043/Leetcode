class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1],[1,1]]
        for i in range(2,numRows):
            res.append([1]*(i+1))
            for j in range(1,i):
                res[i][j] = res[i-1][j] + res[i-1][j-1]
        return res[:numRows]
