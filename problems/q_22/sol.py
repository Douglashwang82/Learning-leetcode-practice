class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        maximumLength = 2*n
        output = []
        
        def isValid(left, right):
            return False if right > left or left > maximumLength//2 else True

        def dfs(path,left_pars,right_pars):
            if isValid(left_pars, right_pars):
                if len(path) == maximumLength:
                    output.append(path)

                if len(path) < maximumLength:
                    dfs(path + "(", left_pars + 1, right_pars)
                    dfs(path + ")", left_pars, right_pars + 1) 
            
        dfs("", 0, 0)
        return output