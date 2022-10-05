#경로탐색(그래프 DFS)
def dfs(v):
    global cnt
    if v == n:
        cnt += 1
        for i in path:
            print(i, end=' ')
        print()
    else:
        for i in range(1, n+1):
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                dfs(i)
                path.pop()
                ch[i] = 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    g = [[0] * (n+1) for _ in range(n+1)]
    cnt = 0
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    ch = [0] * (n+1)

    path = []
    path.append(1)
    ch[1] = 1
    dfs(1)
    print(cnt)
    # for i in range(1, n+1):
    #     for j in range(1, n+1):
    #         print(g[i][j], end=' ')
    #     print()
