#피자 배달 거리(DFS:삼성역량평가)
def dfs(l,s):
    global res
    if l == m:
        sum = 0
        for j in range(len(hs)):
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            for x in cb:
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis,abs(x1-x2)+abs(y1-y2))
            sum += dis

        if sum < res:
            res = sum


    else:
        for i in range(s, len(pz)):
            cb[l] = i
            dfs(l+1, i+1)
if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    #집 좌표정보
    hs = []
    #피자집 좌표정보
    pz = []
    cb = [0]*m
    res = 2147000000
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                hs.append((i,j))
            elif board[i][j] == 2:
                pz.append((i,j))

    dfs(0,0)

    print(res)
