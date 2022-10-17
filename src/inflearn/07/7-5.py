#동전 분배하기
def dfs(l):
    global res
    if l == n:
        cha = max(money) - min(money)
        if cha < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) != 3:
                res = cha

    else:
        for i in range(3):
            money[i] += c[l]
            dfs(l+1)
            money[i] -= c[l]

if __name__ == '__main__':
    n = int(input())
    c = list()
    res = 2147000000
    money = [0] * 3
    for _ in range(n):
        p = int(input())
        c.append(p)
    dfs(0)
    print(res)