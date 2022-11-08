t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    s = 0
    cnt = 0
    b = []
    for i in range(n):
        s = 0
        for j in range(n):
            if board[i][j] == 1:
                s += 1
            else:
                b.append(s)
                s = 0
        b.append(s)
    for i in range(n):
        s = 0
        for j in range(n):
            if board[j][i] == 1:
                s += 1
            else:
                b.append(s)
                s = 0
        b.append(s)
    cnt += b.count(3)
    print(f'#{test_case} {cnt}')