#by using in built function
class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ""
        for i in s:
            if i.isalnum():
                news += i.lower()
        return news == news[::-1]
