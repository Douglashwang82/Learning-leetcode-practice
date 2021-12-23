class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def tree_search(cand, curr, target):
            print(cand, curr, target)
            new_cand = []
            for c in cand:
                if curr:
                    if target  == c and c >= curr[-1]:
                        ans.append(curr + [c])
                else:
                    if target  == c:
                        ans.append(curr + [c])
                if target - c > 0:
                    new_cand.append(c)
            
            for nc in new_cand:
                tree_search(new_cand, curr + [nc], target - nc)

        tree_search(candidates, [], target)
        return  ans