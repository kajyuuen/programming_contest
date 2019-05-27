INF = float("inf")

def i_inpl(): return int(input())
def s_inpl(): return map(int,input().split())
def l_inpl(): return list(map(int, input().split()))

class Edge:
    def __init__(self, from_edge, to_edge, cost):
        self.from_edge = from_edge
        self.to_edge = to_edge
        self.cost = cost

def bellman_ford(start, edges, node_num):
    N = len(edges)
    d = [INF] * node_num
    d[start] = 0
    for i in range(N):
        update_flag = False
        for j in range(N):
            edge = edges[j]
            if edge.from_edge != INF and d[edge.to_edge] > d[edge.from_edge] + edge.cost:
                d[edge.to_edge] = d[edge.from_edge] + edge.cost
                update_flag = True
                if i == N-1:
                    print("負のコスト閉路あり")
        if not update_flag:
            break
    return d

if __name__ == "__main__":
    # https://atcoder.jp/contests/abc016/tasks/abc016_3
    N, M = s_inpl()

    edges = []
    for _ in range(M):
        a, b = s_inpl()
        a, b = a-1, b-1
        edges.append(Edge(a, b, 1))
        edges.append(Edge(b, a, 1))

    for i in range(N):
        print(bellman_ford(i, edges, N))