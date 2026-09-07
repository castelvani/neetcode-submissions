class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        mapS = {}
        mapT = {}

        for i in range(len(s)):
            if s[i] in mapS:
                mapS[s[i]] = mapS[s[i]] + 1
            else:
                mapS[s[i]] = 1
            
            if t[i] in mapT:
                mapT[t[i]] = mapT[t[i]] + 1
            else:
                mapT[t[i]] = 1

        for val in mapS:
            if mapS[val] != mapT.get(val, 0):
                return False

        return True


