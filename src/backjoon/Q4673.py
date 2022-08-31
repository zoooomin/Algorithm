def find_self_num():
    n = 1
    num = [x for x in range(1,10001)]
    not_self_num = []
    while(n < 10001):
        if n < 10:
            res = n + n
        else:
            list_num = [int(a) for a in str(n)]
            res = n + sum(list_num)
        not_self_num.append(res)
        n = n + 1
    self_num = list(set(num) - set(not_self_num))
    self_num.sort()
    for i in self_num:
        print(i)

find_self_num()