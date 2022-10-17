#휴가(DFS)
def dfs(l, sum):
    global res
    if l == n+1:
        if sum > res:
            res = sum
    else:
        if l + tlist[l] <= n+1:
            dfs(l+tlist[l], sum+plist[l])

        dfs(l+1, sum)

if __name__ == '__main__':
    n = int(input())
    tlist = list()
    plist = list()
    for i in range(n):
        t, p = map(int,input().split())
        tlist.append(t)
        plist.append(p)
    res = -2147000000
    tlist.insert(0, 0)
    plist.insert(0, 0)
    dfs(1, 0)
    print(res)