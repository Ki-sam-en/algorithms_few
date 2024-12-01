from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs[0]) == 0 or len(strs[1]) == 0 or len(strs[2]) == 0: return ""

        f0 = strs[0]
        f1 = strs[1]
        f2 = strs[2]

        h = ""

        for i in range(len(f0)):
            if len(f0) == 1 or len(f1) == 1 or len(f2) == 1: 
                if f0[i] == f1[i] and f0[i] == f2[i]:
                    h += f0[i]
                    return h
                else:
                    return h
            if f0[i] == f1[i] and f0[i] == f2[i]:
                h += f0[i]
            else:
                return h
            
        return h
             