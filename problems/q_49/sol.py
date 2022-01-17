class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        
        for s in strs:
            temp = "".join(sorted(s))
            if res.get(temp) != None:
                res[temp].append(s)
            else:
                res[temp] = [s]
        res = [res[li] for li in res]
        
        return res