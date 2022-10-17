#알파코드
def dfs(l, p):
    global cnt
    if l == n:
         cnt += 1
         for j in range(p):
             print(chr(64+res[j]),end='')
         print()
    else:
        for i in range(1, 27):
            if code[l] == i:
                res[p] = i
                dfs(l+1, p+1)
            elif i>=10 and code[l] == i//10 and code[l+1] == i%10:
                res[p] = i
                dfs(l+2, p+1)

if __name__ == '__main__':
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1) #꼭 해야함 26까지 돌기 때문에 마지막 숫자가 4인경우 참이 되지 못함: 몫이 4가 될 수 없기 때문에
    res = [0] * (n+3)
    cnt = 0
    dfs(0,0)
    print(cnt)