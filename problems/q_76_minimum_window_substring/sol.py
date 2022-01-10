class Solution:
    def minWindow(self, s: str, t: str) -> str:
        frequent_t = dict()
        
        for char in t:
            if not frequent_t.get(char):
                frequent_t[char] = 1
            else:
                frequent_t[char] += 1
        
        left = 0
        right = -1
        needed = len(t)
        res_l = 0
        res_r = len(s) + 1
        
        while right < len(s):
            if needed == 0:
                curr = right - left + 1
                minimum = res_r - res_l + 1
                if curr < minimum:
                    res_l = left
                    res_r = right
                if frequent_t.get(s[left]) != None:
                    frequent_t[s[left]] += 1
                    if frequent_t[s[left]] > 0:
                        needed += 1
                left += 1
            else:
                right += 1
                if right < len(s):
                    if frequent_t.get(s[right]) != None:
                        frequent_t[s[right]] -= 1
                        if frequent_t[s[right]] >= 0:
                            needed -= 1
        return s[res_l:res_r + 1] if res_r - res_l + 1 <= len(s) else ""