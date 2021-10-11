"""
    Working Piceses:
        1. pattern matching
    Directions:
        1. Dynamic programming - O(n^2)
            a. Initial the dp table
            b. boundaries set up
            c. iteration rules.
        2. After looking the discussion, there is a better solution can solve the question in O(mn)
            -> Backtracking

"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp_table = [[False for i in range(len(s) + 1)] for i in range(len(p) + 1)]
        dp_table[0][0] = True
        for i in range(len(p)):
            if p[i] == "*":
                dp_table[i + 1][0] = dp_table[i][0]
       
        for i in range(1,len(dp_table[0])):
            for j in range(1,len(dp_table)):
                if p[j - 1] == "*":
                    dp_table[j][i] = dp_table[j][i - 1] or dp_table[j - 1][i]
                if p[j - 1] == "?":
                    dp_table[j][i] = dp_table[j - 1][i - 1]
                if p[j -1] == s[i - 1]:
                    dp_table[j][i] = dp_table[j - 1][i - 1]
        return dp_table[-1][-1]

    def isMatch2(self, s, p):
        if not s and not p: return True   # s and p = null
        if not s and p:                   # s = null
            if p[0] == "*":
                return self.isMatch2("", p[1:])
            else:
                return False
        if s and not p:
            return False
        if p[0] in (s[0], "?"):
            return self.isMatch2(s[1:], p[1:])
        if p[0] == "*":
            mybool = self.isMatch2(s, p[1:])
            while s and not mybool:
                s = s[1:]
                mybool = self.isMatch2(s, p[1:])
            return mybool
        return False
# class Solution:
#     def isMatch(self, s, p):
#         if not s and not p: return True   # s and p = null
#         elif not s and p:                   # s = null
#             if p[0] == "*":
#                 return self.isMatch("", p[1:])
#             else:
#                 return False
#         elif s and not p:
#             return False
#         elif p[0] in (s[0], "?"):
#             return self.isMatch(s[1:], p[1:])
#         elif p[0] == "*":
#             mybool = self.isMatch(s, p[1:])
#             while s and not mybool:
#                 s = s[1:]
#                 mybool = self.isMatch(s, p[1:])
#             return mybool
#         return False
# class Solution:
#     def isMatch(self, s, p):
#         s_p = p_p = 0
#         s_saved =  p_saved = None
#         s_end = len(s)
#         p_end = len(p)
        
#         while s_p < s_end:
#             if p_p < p_end and p[p_p] in (s[s_p], "?"):
#                 s_p += 1
#                 p_p += 1
#             elif p_p < p_end and p[p_p] == "*":
#                 s_saved, p_saved = s_p + 1, p_p
#                 p_p += 1
#             elif s_saved is not None:
#                 s_p = s_saved
#                 p_p = p_saved
#             else:
#                 return False
#         for i in p[p_p:]:
#             if i != "*":
#                 return False
#         return True

sol = Solution()
s = "aab"
p = "a*acb"
print(sol.isMatch2(s,p))



