from collections import defaultdict

def dfs(graph, node_start, visited):
    if node_start in visited:
        return visited
    visited.append(node_start)
    for node_end in graph[node_start]:
        dfs(graph, node_end, visited)
    return visited

def main():
    N, M = map(int, input().split())

    graph = defaultdict(list)
    edges = []

    # 無向グラフの表現
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        edges.append((a, b))

    answer = 0
    for a, b in edges:
        # a, b間のエッジの削除
        graph[a].remove(b)
        graph[b].remove(a)

        visited = dfs(graph, 1, [])
        if len(visited)!= N:
            answer += 1

        # エッジの修復
        graph[a].append(b)
        graph[b].append(a)

    print(answer)

if __name__ == '__main__':
    main()
