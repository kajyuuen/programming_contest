class UnionFind:
    
    def __init__(self, N):
        # 初期は全てが根
        self.parent = [ i for i in range(N)]
        self.rank = [0] * N

    # データxが属する木の根を求める
    def root_find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.root_find(self.parent[x])

    # xとyの属する集合を合併
    def unite(self, x, y):
        x_root = self.root_find(x)
        y_root = self.root_find(y)

        if x_root == y_root:
            return 

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1
    
    # xとyが属する集合が一緒かどうか
    def same(self, x, y):
        return self.root_find(x) == self.root_find(y)            


if __name__ == "__main__":
    def l_inpl(): return list(map(int, input().split()))

    N, Q = l_inpl()
    uf = UnionFind(N)

    answers = []
    for _ in range(Q):
        p, a, b = l_inpl()
        if p == 1:
            if uf.same(a, b):
                answers.append("Yes")
            else:
                answers.append("No")
        else:
            uf.unite(a, b)
    
    print("\n".join(answers))