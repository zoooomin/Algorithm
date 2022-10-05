#수들의 조합
def dfs(l, s, p):
    #l: tree level
    #s: sum
    global cnt
    if l == k:
        if s % m == 0:
            cnt += 1
    else:
        for i in range(p, n):
            dfs(l+1, s+a[i], i+1)
if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    dfs(0, 0, 0)
    print(cnt)