# 部分和問題 p34
# (1)
# 4
# 1 2 4 7
# 13
# (2)
# 4
# 1 2 4 7
# 15

def i_inpl(): return int(input())
def s_inpl(): return map(int,input().split())
def l_inpl(): return list(map(int, input().split()))

n = i_inpl()
a = l_inpl()
k = i_inpl()

# iまででsum_valを作る
def dfs(i, sum_val):
    if i == n:
        return sum_val == k
    
    # a[i]を使う場合
    if dfs(i+1, sum_val + a[i]):
         return True

    # a[i]を使わない場合
    if dfs(i+1, sum_val):
        return True

    # a[i]を使う使わないにかかわらずfalseを返す
    return False

if dfs(0, 0):
    print("Yes")
else:
    print("No")