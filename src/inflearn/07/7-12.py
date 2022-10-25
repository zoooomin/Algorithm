#단지 번호 붙이기(DFS)
#행탐색 먼저
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x,y):
    global cnt
    cnt += 1
    board[x][y] = 0 #현재 지점은 방문했음을 표시
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy] == 1:
            dfs(xx, yy)


if __name__ == '__main__':
    n = int(input())
    board=[list(map(int, input())) for _ in range(n)] #띄어쓰기가 되어있지 않기 때문에splitㅏㅅ용 안함
    res = []#cnt를 append할 리스트
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt = 0
                dfs(i, j)
                res.append(cnt)

    #결과 출력
    res.sort() #오름차순정렬
    print(len(res))
    for x in res:
        print(x)
