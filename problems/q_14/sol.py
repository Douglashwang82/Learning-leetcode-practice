'''
    Work pieces:
        1.COMPARING EVERY PIECES?
    
    Directions:
        1. merge sort - divide and conquer
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Stop point
        if len(strs) < 2:
            return strs[0] # given is a list, ["string"]. 
        left = self.longestCommonPrefix(strs[:len(strs)//2])
        right = self.longestCommonPrefix(strs[len(strs)//2:])
        return self.findingPrefixBetweenTwoString(left,right)

    def findingPrefixBetweenTwoString(self, first_string, second_string):
        longest_prefix = ""
        for i in range(min(len(first_string),len(second_string))):
            if first_string[i] == second_string[i]:
                longest_prefix = first_string[:i + 1]
            else:
                break
        return longest_prefix