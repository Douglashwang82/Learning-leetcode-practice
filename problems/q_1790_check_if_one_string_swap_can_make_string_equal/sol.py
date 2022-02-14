class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n != m: return False
        
        count = 0
        first_index = -1
        second_index = -1
        
        for i in range(n):
            if s1[i] != s2[i]:
                count += 1
                if first_index == -1:
                    first_index = i
                else:
                    second_index = i
                    
        if count > 2: return False
        
        if s1[first_index] == s2[second_index] and s1[second_index] == s2[first_index]:
            return True
        return False