class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        rlength = len(grid)
        clength = len(grid[0])
        
        def isValid(x, y):
            if x < 0 or y < 0:
                return False
            if x >= rlength or y >= clength:
                return False
            return True
        
        
        def dfs(x, y):
            visited.add((x, y))
            
            up =[x - 1, y]
            down = [x + 1, y]
            left = [x, y - 1]
            right = [x, y + 1]
            
            for d in [up, down, left, right]:
                if isValid(d[0], d[1]) and grid[d[0]][d[1]] == "1" and (d[0], d[1]) not in visited:
                    dfs(d[0], d[1])
        
        
        
        
        for i in range(rlength):
            for j in range(clength):
                if not (i , j) in visited and grid[i][j] == "1":
                    dfs(i , j)
                    islands += 1
        
        return islands