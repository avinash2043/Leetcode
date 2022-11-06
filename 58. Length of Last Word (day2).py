class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #a=s.strip().split()
        return len(s.strip().split()[-1])
