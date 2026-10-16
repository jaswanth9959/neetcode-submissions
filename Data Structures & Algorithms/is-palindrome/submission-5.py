class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r = len(s)-1

        while l <= r:
            while l<r and not self.isAlNum(s[l]):
                l+=1
            while l<r and not self.isAlNum(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True

    def isAlNum(self, ch):
        return (ord("a") <= ord(ch) <= ord("z")) or (ord("A") <= ord(ch) <= ord("Z")) or (ord("0") <= ord(ch) <= ord("9"))