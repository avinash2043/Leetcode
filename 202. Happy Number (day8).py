class Solution:
    def isHappy(self, n: int) -> bool:
        ans = set()
        while n != 1:
            temp = 0
            for i in str(n):
                temp += int(i)**2
            n = temp
            if n in ans:
                return False
            else:
                ans.add(n)
        return True
