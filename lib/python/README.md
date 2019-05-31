# ライブラリ

## グラフ

### 最短経路問題

- [ベルマンフォード法: 単一始点最短経路問題（負の閉路がある場合）, O(E * V)](./bellman_ford.py)
- [ダイクストラ法: 単一始点最短経路問題（負の閉路がない場合）, O(E * logV)](./dijkstra.py)
    - TODO: 優先度付きキューを用いた実装
- [ワーシャルフロイド法: 全点対最短経路問題, O(V^3)](./warshall_floyd.py)

### 全探索

- 深さ優先探索 (Depth first search)
    - [隣接行列を用いたDFS](./adjacency_matrix_graph_dfs.py)
    - [隣接リストを用いたDFS](./graph_dfs.py)
- 幅優先探索 (Breadth first search)
    - [隣接行列を用いたBFS](./adjacency_matrix_graph_bfs.py)
    - [Dictを用いたBFS](./graph_bfs.py)

## 数学

- [約数列挙](./divisors.py)
- [最大公約数](./gcd.py)
- [最小公倍数](./lcm.py)
- [素因数分解](./factoring.py)
- [MOD計算](./mod.py)
- [エラトステネスの篩](./sieve_of_eratosthenes.py)
- [組み合わせ](./combinations.py)
- [順列](./permutations.py)

## データ構造

- [Union find](./union_find.py)

## 競技プログラミング 典型

- 深さ優先探索 (Depth first search)
    - [迷路探索の場合のDFS](./maze_dfs.py)
