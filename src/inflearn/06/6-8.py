#순열 구하기
def dfs(l):
    global cnt
    if l == m:
        cnt += 1
        for i in res:
            print(i, end=' ')
        print()

    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                res[l] = i
                ch[i] = 1
                dfs(l+1)
                ch[i] = 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    res = [0] * m
    ch = [0] * (n+1)
    cnt = 0
    dfs(0)
    print(cnt)