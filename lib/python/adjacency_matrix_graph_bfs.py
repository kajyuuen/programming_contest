from collections import deque

INF = float("inf")

def i_inpl(): return int(input())
def s_inpl(): return map(int,input().split())
def l_inpl(): return list(map(int, input().split()))

def bfs(G, i, visited = []):
    if len(visited) == 0:
        visited.append(i)
    queue = deque()
    queue.append(i)
    while queue:
        i = queue.popleft()
        for j in range(len(G)):
            if (G[i][j] != INF) and (G[i][j] != 0) and (j not in visited):
                visited.append(j)
                queue.append(j)
    return visited

if __name__ == '__main__':
    # 入力例
    # https://atcoder.jp/contests/abc016/tasks/abc016_3
    N, M = s_inpl()

    # 隣接行列 G, 存在しない辺はINF
    G = [[INF] * N for _ in range(N)]

    # 自身に向かうコストは0
    for i in range(N):
        G[i][i] = 0

    for _ in range(M):
        a, b = s_inpl()
        a, b = a-1, b-1
        G[a][b] = 1
        G[b][a] = 1

    # ある頂点から訪れることができる頂点の列挙
    for i in range(N):
        print(bfs(G, i, []))