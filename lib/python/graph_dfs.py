from collections import defaultdict

def dfs(graph, node_start, visited):
    if node_start in visited:
        return visited
    visited.append(node_start)
    for node_end in graph[node_start]:
        dfs(graph, node_end, visited)
    return visited

if __name__ == '__main__':
    graph = {
        'A' : ['B','S'],
        'B' : ['A'],
        'C' : ['D','E','F','S'],
        'D' : ['C'],
        'E' : ['C','H'],
        'F' : ['C','G'],
        'G' : ['F','S'],
        'H' : ['E','G'],
        'S' : ['A','C','G']
    }
    for node in graph:
        print(dfs(graph, node, []))
