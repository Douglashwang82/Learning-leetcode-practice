"""
    Working pieces:
        1. matching elements

    Directions:
        1. stack
"""
class Solution:
    def isValid(self, s: str) -> bool:
        isvalid = True
        my_stack = []
        target_string = s
        my_dict_left = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        my_dict_right = {
            ")":")",
            "]":"]",
            "}":"}"
        }
        for char in target_string:
            if char in my_dict_left:
                my_stack.append(my_dict_left[char])
            if char in my_dict_right:
                if len(my_stack) > 0:
                    if my_stack.pop() != my_dict_right[char]:
                        isvalid = False
                else:
                    isvalid = False      
        if len(my_stack) > 0:
            isvalid = False
        return isvalid