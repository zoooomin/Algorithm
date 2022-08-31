def check_id(a):
    wrong1 = len(a[:a.find('-')]) != 6
    wrong2 = len(a) != 14
    year = a[:2]
    month = a[2:4]
    s = a[a.find('-')+1]

    if int(s) in [1, 3]:
        sex = '남자'
    else:
        sex = '여자'

    if int(year) in range(00, 21):
        ans = input(('2000년 이후 출생자 입니까? 맞으면 o 아니면 x : '))
        if wrong1 or wrong2:
            repeat_input()
        elif (ans == 'o') & (int(s) not in [3, 4]):
            repeat_input()
        else:
            print(f'{year}년{month}월 {sex}')
    else:
        if wrong1 or wrong2:
            repeat_input()
        else:
            print(f'{year}년{month}월 {sex}')

def repeat_input():
    print('잘못된 번호입니다.\n올바른 번호를 넣어주세요\n')
    a = input('주민번호 입력: ')
    check_id(a)

a = input('주민번호 입력: ')
check_id(a)