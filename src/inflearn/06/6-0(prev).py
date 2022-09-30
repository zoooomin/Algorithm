'''전역변수와 지역변수'''
def dfs():
    a[0] = 7
    print(a)

if __name__ == '__main__':
    a = [1,2,3]
    dfs()
    print(a)