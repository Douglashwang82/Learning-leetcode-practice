class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Soving Process:
            1. First, I thought of each row is one of an arithmetic sequence but when assigned row get larger the complexity of arithmetic sequences rise. So, There must be a better way.
            2. Second, I noticed I could see this zigzag as a big 2D graph with m "zigzags". I maybe can create a function that convert current index to a proper position in zigzags.
                ex:
                row = 3 
                index 1 is in the first position of the first zigzag.
                index 5 is in the first position of the second zigzag.
                
            3. Then, I realized it was no help on reordering the string.
            4. Reodering is base on the rows oder. 
            5. So, I decided to insert each character in its proper row.
            6. Then, join() each rows to be the output.
        """
        if numRows == 1: # Handling the exception
            return s
        
        sep_rows = ["" for i in range(numRows)] # determine numRows rows.
        n_positions = 2*numRows - 2  #nubmer of zigzag positions. ex 1:1, 2:2, 3:5, 4:6,..... 
        
        for i in range(len(s)):
            temp_row = i % n_positions
            target_row = temp_row if temp_row < numRows else n_positions - temp_row 
            sep_rows[target_row] = sep_rows[target_row] + s[i]
        
        return "".join(sep_rows)