class UnionFind(object):
 
    def __init__(self, N):
        self.parent = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N
 
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
 
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
 
        if self.rank[x] < self.rank[y]:
            x, y = y, x
 
        self.size[x] += self.size[y]
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
 
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
    def count(self, x):
        return self.size[self.find(x)]


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
            uf.union(a, b)
    
    print("\n".join(answers))