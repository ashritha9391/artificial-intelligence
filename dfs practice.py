from collections import deque
def dfs(graph, node, v=set()):
    if node not in v:
        print(node, end=" ")
        v.add(node)
        for n in graph[node]: dfs(graph, n, v)

graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
dfs(graph, 2)
#output
2 0 1 3 
