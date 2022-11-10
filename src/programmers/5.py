#회전 배열
t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    num = [list(input().split()) for _ in range(n)]
    ans_board = [[0] * n for _ in range(n)]
    cnt = 0
    for k in range(3):#90,180,270회전//3번 회전
        n_num = [[0] * n for _ in range(n)]  # 회전한 배열
        for i in range(n):
            board = [b[i] for b in num]
            n_num[i] = board[::-1]
            ans_board[cnt][i] = ''.join(n_num[i])
        cnt += 1
        num = n_num
    print(f'#{test_case}')
    for i in range(n):
        for j in range(3):
            print(ans_board[j][i], end=' ')
        print()
