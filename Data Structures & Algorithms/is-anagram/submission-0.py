class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashS = {}
        hashT = {}
        for i in range(len(s)):
            if s[i] not in hashS:
                hashS[s[i]] = 1
            else:
                hashS[s[i]] += 1
            if t[i] not in hashT:
                hashT[t[i]] = 1
            else:
                hashT[t[i]] += 1
        return hashS == hashT