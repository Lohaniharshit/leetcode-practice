class Solution1: # fail
    def isAnagram(self, s: str, t: str) -> bool:
        a=[]
        if len(s)==len(t):
            for i in s:
                a.append(i)
            for j in t:
                if j not in a:
                    return False
            return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        return sorted(s)==sorted(t)
# from collections import Counter
