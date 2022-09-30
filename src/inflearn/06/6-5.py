#바둑이 승차
def dfs(l, sum, tsum):
    global result
    if sum + (total-tsum)<result:
        #sum : 지금까지 더한 값
        #total-tsum : 앞으로 더해야 할 값
        #result : 앞에서 마지막 레벨까지 탐색을 끝낸 결과값
        return
    if sum > c:
        return
    if l == n:
        if sum > result:
            result = sum
    else:
        dfs(l+1, sum+w[l], tsum+w[l])
        dfs(l+1, sum, tsum+w[l])


if __name__ == '__main__':
    c, n = map(int, input().split())
    w = [0] * n
    result = -2147000000

    for i in range(n):
        w[i] = int(input())

    total = sum(w)
    dfs(0, 0, 0)
    print(result)