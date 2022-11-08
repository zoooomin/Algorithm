#계단오르기(메모이제이션)
def dfs(stair):
    if stair == 1 or stair == 2:
        return stair
    else:
        dy[stair] = dfs(stair-1) + dfs(stair-2)
        return dy[stair]
if __name__ == '__main__':
    n = int(input())
    dy = [0] * (n+1)
    print(dfs(n))