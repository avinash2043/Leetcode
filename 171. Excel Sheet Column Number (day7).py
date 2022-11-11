class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = columnTitle[::-1]
        ans = 0
        for i in range(len(columnTitle)):
            ans += (26**i)*int(ord(columnTitle[i])-64)
        return ans
