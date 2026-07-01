class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a = ""
        for i in range(len(s)-1,-1,-1):
            if s[i].isalnum():
                a += s[i]
        return a == a[::-1]
