
    
graph = [[["white", False] for _ in range(5)] for _ in range(3)]
r = "red"
b = "blue"
y = "yellow"

graph[0][0] = [r, False]
graph[0][1] = [b, False]
graph[0][2] = [b, False]
graph[0][3] = [r, False]
graph[0][4] = [r, False]

graph[1][0] = [r, False]
graph[1][1] = [r, False]
graph[1][2] = [y, False]
graph[1][3] = [y, False]
graph[1][4] = [r, False]

graph[2][0] = [r, False] 
graph[2][1] = [y, False]
graph[2][2] = [y, False]
graph[2][3] = [r, False]
graph[2][4] = [r, False]
def printGraph(graph):
    for i in range(3):
        print(graph[i])


def dfs(i, j):
    stack = []
    number = 0
    stack.append([i, j])
    while stack:
        curr = stack.pop()
        graph[curr[0]][curr[1]][1] = True
        number += 1
        for x in range(curr[0] - 1, curr[0] + 2):
            for y in range(curr[1] - 1, curr[1] + 2):
                if x >= 0 and y >= 0 and x < 3 and y < 5:
                    if graph[x][y][1] == False and graph[x][y][0] == graph[i][j][0]:
                        stack.append([x, y])
                        graph[x][y][1] = True
        print(stack)
    return number
            
maximum = 0

for i in range(3):
    for j in range(5):
        print('originMaximum:', maximum)
        if not graph[i][j][1]:
            maximum = max(maximum, dfs(i, j))
        printGraph(graph)
        print(maximum)
print(maximum)