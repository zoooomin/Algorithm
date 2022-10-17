#동전 바꿔주기(DFS)
def dfs(l, sum):
    global cnt
    if sum > t:
        return
    if l == k:
        if sum == t:
            cnt += 1
    else:
        for i in range(cn[l]+1):
            dfs(l+1, sum+cv[l]*i)
if __name__ == '__main__':
    t = int(input())
    k = int(input())
    cv = list() #동전 금액
    cn = list() #동전 개수
    for i in range(k):
        a, b = map(int, input().split())
        cv.append(a)
        cn.append(b)
    cnt = 0
    dfs(0,0)
    print(cnt)