class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_1 = dict()
        freq_2 = dict()
        
        for c in s:
            if freq_1.get(c):
                freq_1[c] += 1
            else:
                freq_1[c] = 1
        
        for c in t:
            if freq_2.get(c):
                freq_2[c] += 1
            else:
                freq_2[c] = 1
        
        for k in freq_1:
            if freq_1.get(k) != freq_2.get(k):
                return False
        
        return len(s) == len(t)