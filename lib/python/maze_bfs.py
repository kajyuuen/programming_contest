# https://atcoder.jp/contests/abc007/tasks/abc007_3
from collections import deque

def s_inpl(): return map(int,input().split())

# 四方向: 右, 下, 左, 上
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

def bfs(field, number_of_moves, sy, sx):
    queue = deque([[sy, sx]])
    number_of_moves[sy][sx] = 0
    while queue:
        y, x = queue.popleft()
        current_number_of_move = number_of_moves[y][x]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if inside(ny, nx, H, W) and \
                field[ny][nx] == "." and \
                number_of_moves[ny][nx] == -1:
                number_of_moves[ny][nx] = current_number_of_move + 1
                queue.append([ny, nx])
    return number_of_moves


if __name__ == "__main__":
    H, W = s_inpl()
    sy, sx = s_inpl()
    gy, gx = s_inpl()
    sy, sx, gy, gx = sy-1, sx-1, gy-1, gx-1
    field = [ input() for _ in range(H) ]

    # かかった手数が-1のとき，未探索
    number_of_moves = [ [-1] * W for _ in range(H) ]
    number_of_moves = bfs(field, number_of_moves, sy, sx)
    print(number_of_moves[gy][gx])