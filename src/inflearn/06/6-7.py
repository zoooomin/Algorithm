#동전 교환
def dfs(l, sum):
    global res
    if l > res:
        return
    if sum > m:
        return
    elif sum == m:
        if l < res:
            res = l
    else:
        for i in range(n):
            dfs(l+1, sum+a[i])

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    res = 2147000000
    a.sort(reverse=True)
    dfs(0, 0)
    print(res)