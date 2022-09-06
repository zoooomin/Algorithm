#이분 검색
#포인트 변수 2개(lt, rt)
'''
mid = (lt + rt)//2
m과 mid를 비교
a[mid] == m가 아니고 a[mid]보다 작다면
rt = mid-1
a[mid] == m가 아니고 a[mid]보다 크다면
lt = mid +1
 '''
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort() #정렬을 먼저 한다.

lt = 0 #배열의 맨처음을 가리킨다.
rt = n-1 #배열의 마지막을 가리킨다.
while lt<=rt: #lt는 항상 왼쪽, rt는 항상 오른쪽, 같을 수도 있다.아닐경우 탈출
    mid = (lt + rt) // 2 #mid는 lt와 rt의 중간
    if a[mid] == m: #같을 경우 출력
        print(mid + 1)
        break
    elif a[mid] > m: #mid값이 더 클 경우 rt는 mid 왼쪽으로 이동
        rt = mid - 1
    else: #mid값이 더 작을 경우 lt는 mid 오른쪽으로 이동
        lt = mid + 1
















