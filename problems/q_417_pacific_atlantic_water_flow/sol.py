"""
Works:
    1. Finding Pathes
    2. Intersection
    
Directions:
    1. DFS or BFS

Conclusion:
    ***
    I first tried to apply dfs() in every node and change the start node's state by using the end nodes from the founded paths. 
    ***
    
    This is a terrible idea. The problem became more and more complex and really hard to read and also write...
    I have learned that if the logic becomes more and more complex and untrackable. It must be a bad idea. Just rip it and start from the beginning.
    
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pset = set()
        aset = set()
        rlength = len(heights)
        clength = len(heights[0])
        
        def isValid(x, y):
            """
            Is a Valid node on the board?
            """
            if x < 0 or y < 0:
                return False
            if x >= rlength or y >= clength:
                return False
            return True
        
        def dfs(x, y, theSet):
            """
            1. Add the node to the related set if it hasnt been visited.
            2. Check its neighbors if they allows water flow.
                if yes, dfs(neighbor).
                if no, do nothing.
            """
            if (x, y) in theSet:
                return
            
            theSet.add((x, y))
            
            up = [x - 1, y]
            down = [x + 1, y]
            left = [x, y - 1]
            right = [x, y + 1]
            
            for d in [up, down, left, right]:
                if isValid(d[0], d[1]) and heights[x][y] <= heights[d[0]][d[1]]:
                    dfs(d[0], d[1], theSet)
        
        # pacific edges
        for r in range(rlength):
            dfs(r, 0, pset)
        for c in range(clength):
            dfs(0, c, pset)
        
        # atlantic edges
        for r in range(rlength):
            dfs(r, clength - 1,  aset)
        for c in range(clength):
            dfs(rlength - 1, c, aset)
            
        
        # Return cells that in both aset and pset
        return pset.intersection(aset)