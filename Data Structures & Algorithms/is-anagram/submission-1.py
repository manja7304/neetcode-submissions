from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) < len(t) or len(t) < len(s):
            return False

        hashSet_s , hashSet_t = defaultdict(int) , defaultdict(int)

        for index , value in enumerate(s):
            hashSet_s[value] += 1
            hashSet_t[t[index]] +=1 
        
        return True if hashSet_s == hashSet_t else False
        