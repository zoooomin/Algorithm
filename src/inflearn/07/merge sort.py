#(divide and conquer)
#dsort(lt,mid)
#dsort(mid+1,rt)
def dsort(lt, rt):
    if lt < rt:
        mid = (lt + rt) // 2
        dsort(lt,mid)
        # print('l: ',lt, mid)
        dsort(mid+1, rt)
        # print('r: ',mid+1, rt)
        p1 = lt
        p2 = mid + 1
        # print('p1: ',p1,'p2: ',p2)
        tmp = []
        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1 += 1
            else:
                tmp.append(arr[p2])
                p2 += 1
        if p1 <= mid: tmp = tmp + arr[p1:mid+1]
        if p2 <= rt: tmp += arr[p2:rt+1]
        #병합
        for i in range(len(tmp)):
            arr[lt+i] = tmp[i]
if __name__ == '__main__':
    arr = [23,11,45,36,15,67,33,21]
    print('before sort: ',end=' ')
    print(arr)
    dsort(0,len(arr)-1)
    print()
    print('after sort: ',end=' ')
    print(arr)
