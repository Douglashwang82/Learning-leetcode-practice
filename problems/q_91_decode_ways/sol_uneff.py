class Solution:
    def numDecodings(self, s: str) -> int:
        ans = []
        my_dict = {str(i):chr(i + 64) for i in range(1, 27)}

        def my_tree(rs, curr):
            if not rs:
                ans.append(1)
            else:
                oneDigit = my_dict.get(rs[0])

                if oneDigit:
                    my_tree(rs[1:], rs[0])

                if curr:
                    twoDigit = curr + rs[0] if my_dict.get(curr + rs[0]) else None

                    if twoDigit:
                        my_tree(rs[1:], curr +rs[0])
                        
        my_tree(s, [])
        
        return len(ans)

        
            
            
            