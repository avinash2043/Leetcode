class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        c=0
        res=""
        for i in range(max(len(a),len(b))):
            if i < len(a):
                A = int(a[i])
            else:
                A = 0
            if i < len(b):
                B = int(b[i])
            else:
                B = 0
            ans = A+B+c
            res = str(ans%2) + res
            c = ans//2
        if c == 1:
            return "1"+res
        return res
