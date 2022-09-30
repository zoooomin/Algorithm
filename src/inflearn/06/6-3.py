#부분집합 구하기
def dfs(x):
    if x == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i,end=' ')
        print()
    else:
        ch[x] = 1
        dfs(x+1)
        ch[x] = 0
        dfs(x+1)
if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n+1)
    dfs(1)