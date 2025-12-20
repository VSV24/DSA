class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashed = {}
        hashed2 = {}
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] in hashed:
                    hashed[s[i]] += 1
                else:
                    hashed[s[i]] = 0
                    
                if t[i] in hashed2:
                    hashed2[t[i]] += 1
                else:
                    hashed2[t[i]] = 0
                    
            if hashed == hashed2:
                return True
            else:
                False
        return False

            