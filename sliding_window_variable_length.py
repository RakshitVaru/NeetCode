class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L=0
        length=0
        new_s=''
        for R in range(len(s)):
            if s[R] in new_s:
                L=R
            new_s+=s[R]
            length= max(R-L+1, length)
        return length