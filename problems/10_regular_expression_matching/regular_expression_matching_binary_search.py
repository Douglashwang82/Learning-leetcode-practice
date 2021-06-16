class Solution:
    def isMatch2(self, s: str, p: str) -> bool:
        if s == p[0]:
            return True
        if p[0] == ".":
            return True

        return False
    def isMatch(self, s: str, p: str) -> bool:
        """
        Solving Process:
            1. First, I thought of base two ways. One is base on the string and iterate the pattern. Another is base one the pattern and iterate the string.
            2. Not very clear in this thinking.
            3. Second, I decided to first separate the pattern into small pices and store them in to an array, small_patterns[m], m piecese patterns.
            4. Then, I realized it still come up with problems that dealing with "*" sign.
            5. Search discussion answers:
                1. Construct a Binary Tree - brute force. O(2^n) because add one "*" sign get two new possible branches. (include it and not include it)
                2. Dynamic Programming - O(2^n)
        Regular Expression Matching:
            Match?
                a_string
                a_pattern 
            __________________
            Everything Start from the base
                Zero cases:
                    len(s) == 0 ?
                    len(p) == 0 ?
                Atom cases:
                    s: normal
                    p: pattern with no "*"
                    p: pattern with "*"
            __________________
            Brute force approach:
                Binary Search: O(2^n) (Recursively)
        """
        # Stop point (Zero cases handling)
        # out of s, out of p
        # out of s
        # out of p
        if not p:
            return not s
        
        match_first = bool(s) and p[0] in (s[0], '.')

        # recursive part
        # Included "*"
        # either use current a* or skip this a*.
        if len(p) >= 2 and p[1] == "*":
            return (match_first and self.isMatch(s[1:], p)) or (self.isMatch(s, p[2:]))
        
        # not included "*"
        return match_first and self.isMatch(s[1:],p[1:])
s = Solution()

sample = "mississippi"
pattern = "mis*is*p*."
print(s.isMatch(sample,pattern))