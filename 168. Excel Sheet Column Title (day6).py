class Solution:
    def convertToTitle(self, n: int) -> str:
        s=""
        while n>0:
            n-=1
            rem = n%26
            n = n//26
            s=chr(rem+65)+s
        return s
