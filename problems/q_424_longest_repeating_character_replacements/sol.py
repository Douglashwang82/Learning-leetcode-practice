class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency_table = dict()
        left = local_maximum = global_maximum = 0
        
        for right in range(len(s)):
            if frequency_table.get(s[right]):
                frequency_table[s[right]] += 1
            else:
                frequency_table[s[right]] = 1
            
            local_maximum = max(local_maximum, frequency_table[s[right]])
            substringlength = right - left + 1
            
            if substringlength - local_maximum <= k:
                global_maximum = max(global_maximum, substringlength)
            else:
                frequency_table[s[left]] -= 1
                left += 1
        
        return global_maximum