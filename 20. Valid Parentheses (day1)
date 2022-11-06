class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={
            "(" : ")" , "[" : "]" , "{" : "}"
        }
        for i in s:
            if i in d.keys():
                stack.append(i)
            elif len(stack)== 0 or d[stack[-1]] != i:
                return False
            else:
                stack.pop()
        return len(stack) == 0
