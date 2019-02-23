from collections import defaultdict
from collections import deque
def bfs(graph, node_start, visited):
    queue = deque(node_start)
    while queue:
        node_end = queue.popleft()
        for node_neighbour in graph[node_end]:
            if node_neighbour not in visited:
                visited.append(node_neighbour)
                queue.append(node_neighbour)
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
        print(bfs(graph, node, []))
