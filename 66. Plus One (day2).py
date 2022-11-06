class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        x=[]
        for i in digits:
            s+=str(i)
        s=str(int(s)+1)
        for i in range(len(s)):
            x.append(s[i])
        return x
