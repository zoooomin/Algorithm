#조합 구하기
def dfs(l, s):
    global cnt
    if l == m:
        cnt += 1
        for i in range(l):
            print(res[i], end=' ')
        print()
    else:
        for i in range(s, n+1):
            res[l] = i
            dfs(l+1, i+1) #주의! s가 아니라 i!
if __name__ == '__main__':
    n, m = map(int, input().split())
    cnt = 0
    res = [0] * n
    dfs(0, 1)
    print(cnt)