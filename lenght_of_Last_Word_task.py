class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = len(s.split()[-1])
        return s 