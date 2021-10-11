class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Solving Process:
            1. First, I know I can solve this by iterate every character in the string. And take the position as the middle to check if it is a palindorme with 
               with two cases. One is palindrome with odd length. Another is palindrome with even length. It is an O(n logn) algorithm.
            2. Second, I tried to solve this problem using dynamic programming concepts. And I think I can only figure out an O(n^2) algorithm.
            3. (...)
        """
        length = len(s)
        dynamic_board = [[0 for i in range(length)] for i in range(length)]
        start = 0
        end = 0
        maximum = 0
        # Preprocess the dynamic board
        # substing length:
        # length = 0
        if length == 0:
            return "Invalid Input with blank"
        
        # length = 1
        for i in range(length):
            dynamic_board[i][i] = 1 # for a,....
            if dynamic_board[i][i]:
                maximum = 1
                start = 0
                end = 0

        # length = 2
        for i in range(length - 1): # An can not be the start index. So, minus 1.
            if s[i] == s[i + 1]:    # for aa,....
                dynamic_board[i][i + 1] = 1
            if dynamic_board[i][i + 1]:
                maximum = 2
                start = i
                end = i + 1

        # length = 3
        for i in range(length - 2): # Same reason of handling length 2 substrings.
            if s[i] == s[i + 2]:    # for aba...
                dynamic_board[i][i + 2] = 1
            if dynamic_board[i][i + 2]:
                maximum = 3
                start = i
                end = i + 2
        # Main Processing
        # substring lengths: 4 to n 
        for i in range(4, length + 1):      # length + 1, because length of the whole string needs to be included.
            for j in range(length - i + 1): # (length - i + 1), handling the boarder. 
                if s[j] == s[j + i - 1] and dynamic_board[j + 1][j + i - 2] == 1: # see "photo"
                    dynamic_board[j][j + i - 1] = 1
                if dynamic_board[j][j + i - 1]: # If this substring is a palindrome.
                   if i > maximum:
                       maximum = i
                       start = j
                       end = j + i - 1
        return s[start:end + 1]
