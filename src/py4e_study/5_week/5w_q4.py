day31 = [1,3,5,7,8,10,12]
day30 = [4,6,9,11]
day28 = [2]
weekday = ['월', '화', '수', '목', '금', '토', '일']
def after_100(m, d, yy):
    '''100일 이후의 월, 일, 요일을 구하는 함수'''
    day = d + 100 #100일 더하기

    while day > 31:
        if m in day31:
            day -= 31
        elif m in day30:
            day -= 30
        elif m in day28:
            day -= 28
        m += 1 #각 월마다 가진 일수를 빼준 후 월을 더해서 다음달이 되게 해준다.

        if m > 12:
            m -= 12 #12월이 넘는 13일 경우 1월로 돌아갈 수 있게 해줌

    day -= 1 #당일 부터 d-da가 시작되기 때문에 1을 빼줌

    #100일 후의 요일 구하기
    #100일 : 14주하고 2일->당일은 빼줘야하므로 14주하고 1일->사귄날의 바로 다음 요일
    if weekday.index(yy) == 6:
        d_day_yy = weekday[0] #일요일의 다음요일이 월요일이 되도록
    else:
        day_index = weekday.index(yy)
        d_day_yy = weekday[day_index + 1]

    print(f'100일 후는 {m}월 {day}일 {d_day_yy}요일')

after_100(8, 15, '월')