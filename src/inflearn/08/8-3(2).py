#돌다리 건너기(메모이제이션bottom_up)
def dfs(step):
    #이미 알고 있는 값으로 가지를 뻗지 않기 위한 조건
    if dy[step] > 0:
        return dy[step]
    if step == 1 or step == 2:
        return step
    else:
        dy[step] = dfs(step-1) + dfs(step-2)
        return dy[step]

if __name__ == '__main__':
    n = int(input())
    dy = [0] * (n+2)
    print(dfs(n+1))