class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Solving Process:
            1. First, I know I can solve this by iterate every character in the string. And take the position as the middle to check if it is a palindorme  
               with two cases. One is palindrome with odd length. Another is palindrome with even length. It is an O(n log n) algorithm since we compare
               up to half of len(s) in every index.
            2. Second, I tried to solve this problem using dynamic programming concepts. And I think I can only figure out an O(n^2) algorithm.
            3. Then, an O(n^2) is not good enough for passing the examination.
            4. Back to use the first method with O(n log n), which is check every index in the string if it is a middle of a palindrome.
        """
        p_list = []
        maximum = 0
        ind = 0
        for i in range(len(s)):
            p_list.append(self.find_the_maximum_palindrome(s,i))
            if p_list[i] > maximum:
                maximum = p_list[i]
                ind = i
        if maximum % 2 != 0:
            return s[ind- (maximum)//2:ind+(maximum)//2 + 1]
        else:
            return s[ind-(maximum)//2 + 1:ind+(maximum)//2 + 1]

    def find_the_maximum_palindrome(self, s:str, ind: int): 
        length = len(s)
        maximum_odd = 1
        maximum_even = 0
        # odd length
        start = ind - 1
        end = ind + 1
        while start >= 0 and end < length:
            if s[start] == s[end]:
                maximum_odd += 2
            else:
                break
            start = start - 1
            end = end + 1

        # even length
        start = ind
        end = ind + 1
        while start >= 0 and end < length:
            if s[start] == s[end]:
                maximum_even += 2
            else:
                break
            start = start - 1
            end = end + 1
        return max(maximum_even, maximum_odd)
        