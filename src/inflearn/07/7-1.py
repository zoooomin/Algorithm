#최대점수 구하기 (DFS)
def dfs(l, sum, time):
    global res
    if time > m:
        return
    if l == n:
        if sum > res:
            res = sum
    else:
        dfs(l+1, sum + pv[l], time + pt[l])
        dfs(l+1, sum, time) #문제를 안푸는 경우

if __name__ == '__main__':
    n, m = map(int, input().split())
    pv = list()
    pt = list()
    for i in range(n):
        a, b = map(int,input().split())
        pv.append(a) #점수
        pt.append(b) #시간
    res = -2147000000
    dfs(0, 0, 0)
    print(res)