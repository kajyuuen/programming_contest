INF = float("inf")

def i_inpl(): return int(input())
def s_inpl(): return map(int,input().split())
def l_inpl(): return list(map(int, input().split()))

# グラフGにおいてstartから各頂点に行くまでの最小コストを計算する
def dijkstra(G, start):
    # 初期化
    N = len(G)

    cost = [INF] * N # startから各頂点への最小コスト
    visited = [False] * N # 選択した頂点を記録する
    prev = [False] * N # 出発点から各頂点への経路を保存(なくても動く)

    cost[start] = 0
    prev[start] = start
    current_point = start

    while True:
        min_point = -1 # 出発点から最小コストの点, -1は未探索
        min_cost = INF # 出発点から最小コストの点に行くまでのコスト
        visited[current_point] = True
        # 頂点の選択
        for i in range(N):
            # 探索済み
            if visited[i]: continue
            # current_pointからiまでの辺がある場合
            if G[current_point][i] != INF:
                # current_pointまでの最小コストとcurrent_pointからiまでのコストの和
                current_to_i_cost = cost[current_point] + G[current_point][i]
                if cost[i] > current_to_i_cost:
                    cost[i] = current_to_i_cost
                    prev[i] = current_point
            if min_cost > cost[i]:
                min_cost = cost[i]
                min_point = i
        current_point = min_point
        if current_point == -1: break

    return cost



if __name__ == "__main__":
    # https://atcoder.jp/contests/abc016/tasks/abc016_3
    N, M = s_inpl()

    # 隣接行列 G, 存在しない辺はINF
    G = [[INF] * N for _ in range(N)]

    for _ in range(M):
        a, b = s_inpl()
        a, b = a-1, b-1
        G[a][b] = 1
        G[b][a] = 1

    for i in range(N):
        print(dijkstra(G, i).count(2))