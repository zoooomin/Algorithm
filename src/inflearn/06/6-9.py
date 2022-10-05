#수열 추측하기
import sys

def dfs(l, s):
    if l == n and s == f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[l] = i
                dfs(l+1, s + (p[l] * b[l]))
                ch[i] = 0

if __name__ == '__main__':
    n, f = map(int, input().split())
    p = [0] * n # 순열 저장
    b = [1] * n # 이항 계수
    ch = [0] * (n+1)
    s = 0
    for i in range(1, n):
        b[i] = (b[i-1] * (n-i)) // i
    dfs(0, 0)
