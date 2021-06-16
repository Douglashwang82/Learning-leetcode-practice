
import numpy as np
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Sovling Process:
        1. I though of brute force comparison in the first place but instanly knowing that is not the purpose of this problem.
        2. Stuck days for solving thie problem. Really frustrating.
        3. Decided for looking discussion.
        4. There are two common approaches "Binary Search" and "Dynamic Programming"
        5. DP approach is more efficient. with O(n*2) (44ms)
        6. Learning DP:
            1. DP always include a table (or array).
            2. Use the basic results to computer the target result.
            3. In this case, our target result is "Is s[0:len(s)] in the set of p[0:len(p)] ?"
            4. In DP, we need to set up some basic rows in the table.
            5. First, Set a table with dp[len(s)][len(p)] with all False value. and Set the dp[0][0] to be True.
               Second, Figure out how differnet length of patterns matching the ""(empty string) -> the first row in the table.
               Third, Working on the looping part:
                    1. Use different length of p to compare with differnt length of s.
                    2. Two cases(Hard Part):
                        1. the current p[i] = "*"
                            Two cases in this situation:
                                a. Use the current pointed pattern p[i-1:i+1] ->"a*"
                                b. Ignore the current pointed pattern p[i-1:i+1] -> follow the state with p[0:i - 2] 
                        2. the current p[i] in (normal alphabet, ".")
                            this is easy. If dp[j-1][i-1] = TRUE
                            Read a string and read a pattern. If match, dp[j][i] = TRUE
        7. Use package Numpy for better understanding. Remove numpy part can reduce the running time and usage of memory.
        """ 
        # Prepare the dynamic programming table
        # Add one because including empty string row and empty pattern row.
        dp =[[False for i in range(len(p) + 1)] for i in range(len(s) + 1)]
        
        # Case "not s and not p" is TRUE
        dp[0][0] = True

        # Set up the first row of the table which represent different length of pattern and compare them with empty string.
        for i in range(len(p) + 1):
            if i >= 2:
                dp[0][i] = dp[0][i - 2] and p[i - 1] == "*"

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                # Case current pattern = "*"
                # either use current "a*" or ignore it.
                # use case: current string is the same with pattern "a" and current pattern is true on s[j - 1]
                # ignore case: the state is match with p[i - 2](which is ignore the current "a*")
                if p[i - 1] == "*":
                    dp[j][i] = (dp[j - 1][i] and p[i - 2] in (s[j - 1], ".")) or (dp[j][i - 2])

                # Case pattern with normal alphabet or "."
                # current string match the current pattern and the state dp[j-1][i-1] is TRUE
                else:
                    dp[j][i] = dp[j - 1][i - 1] and p[i - 1] in (s[j - 1], ".")
        n = np.array(dp)
        print(n)
        return dp[len(s)][len(p)]
s = Solution()
sample = "mississippi"
pattern = "mis*is*p*."
print(s.isMatch(sample, pattern))