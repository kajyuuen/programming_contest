# 八方向: 右, 下, 左, 上，右上, 右下, 左下, 左上
dy = [0, -1, 0, 1, 1, -1, -1, 1]
dx = [1, 0, -1, 0, 1, 1, -1, -1]

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

H, W = map(int, input().split())
f = []
for _ in range(H):
    S = input()
    f.append(S)

ans = [[0] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        if f[y][x] == "#":
            ans[y][x] = "#"
        else:
            cnt = 0
            for i in range(8):
                ny = y + dy[i]
                nx = x + dx[i]
                if inside(ny, nx, H, W) and f[ny][nx] == "#":
                    cnt += 1
            ans[y][x] = str(cnt)

for line in ans:
    print(*line, sep="")
