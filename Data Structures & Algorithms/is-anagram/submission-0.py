class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ch_array = [0]*26

        if len(s)!= len(t):
            return False
        for i in range(len(s)):
            ch_array[ord(s[i])-ord("a")]+=1
            ch_array[ord(t[i])-ord("a")]-=1
        
        for i in range(26):
            if ch_array[i]!= 0:
                return False
        return True
        