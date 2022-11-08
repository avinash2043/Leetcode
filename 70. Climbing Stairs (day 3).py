class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 1,1
        for i in range(n-1):
            temp = a
            a = a+b
            b = temp
        return a
      
#video link:
#https://www.youtube.com/watch?v=Y0lT9Fck7qI
