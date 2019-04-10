INF = float("inf")

def i_inpl(): return int(input())
def s_inpl(): return map(int,input().split())
def l_inpl(): return list(map(int, input().split()))

def warshall_floyd(G):
    # G[i][j]: iからjへの最短距離
    N = len(G)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])
    return G

if __name__ == "__main__":
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

    G = warshall_floyd(G)
    for row in G:
        print(row.count(2))
