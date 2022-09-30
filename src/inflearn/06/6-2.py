#이진트리 순회(dfs)

def dfs(v):
    if v>7:
        return
    else:
        dfs(v*2)#왼쪽노드
        print(v)
        dfs(v*2+1)#오른쪽노드

if __name__ == "__main__":
    dfs(1)