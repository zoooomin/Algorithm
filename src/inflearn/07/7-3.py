#양팔저울(DFS)
def dfs(l, sum):
    global res
    if l == k:
         if 0<sum<=s:
             res.add(sum) #대칭 구조가 만들어지기 때문에 음수는 제외
    else:
        dfs(l+1, sum+a[l]) #왼쪽
        dfs(l+1, sum-a[l]) #오른쪽
        dfs(l+1, sum)
if __name__ == '__main__':
    k = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    res = set()
    dfs(0, 0)
    print(s-len(res))