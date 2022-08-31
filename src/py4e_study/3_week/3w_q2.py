import random
computer = random.randint(0, 2)
computer_win = 0
computer_lose = 0
you_win = 0
you_lose = 0
same = 0
def rsp(you, cnt):
    global computer_win, computer_lose, you_win, you_lose, same

    if (computer == 0):
        print('컴퓨터 : 가위')
        if (you == 1):
            print('나 : 바위')
            print(f'{cnt}번째 판: ', end=' ')
            print('당신이 이겼습니다!')
            you_win = you_win + 1
            computer_lose = computer_lose + 1
        elif (you == 2):
            print('나 : 보')
            print(f'{cnt}번째 판: ', end=' ')
            print('컴퓨터가 이겼습니다.')
            you_lose = you_lose + 1
            computer_win = computer_win + 1
        else:
            print('나 : 가위')
            print(f'{cnt}번째 판: ', end=' ')
            print('비겼습니다.')
            same = same + 1

    elif (computer == 1):
        print('컴퓨터 : 바위')
        if (you == 0):
            print('나 : 가위')
            print(f'{cnt}번째 판: ', end=' ')
            print('컴퓨터가 이겼습니다.')
            you_lose = you_lose + 1
            computer_win = computer_win + 1
        elif (you == 2):
            print('나 : 보')
            print(f'{cnt}번째 판: ', end=' ')
            print('당신이 이겼습니다!')
            you_win = you_win + 1
            computer_lose = computer_lose + 1
        else:
            print('you : 바위')
            print(f'{cnt}번째 판: ', end=' ')
            print('비겼습니다.')
            same = same + 1

    elif (computer == 2):
        print('컴퓨터 : 보')
        if (you == 0):
            print('나 : 가위')
            print(f'{cnt}번째 판: ', end=' ')
            print('당신이 이겼습니다!')
            you_win = you_win + 1
            computer_lose = computer_lose + 1

        elif (you == 1):
            print('나 : 바위')
            print(f'{cnt}번째 판: ', end=' ')
            print('컴퓨터가 이겼습니다.')
            you_lose = you_lose + 1
            computer_win = computer_win + 1
        else:
            print('나 : 보')
            print(f'{cnt}번째 판: ', end=' ')
            print('비겼습니다.')
            same = same + 1

    print('\n')
    return computer_lose,computer_win,you_lose,you_win,same

def rsp_advanced(games):
    cnt = 1#게임 횟수 카운트
    while games>0:
        you = int(input('가위:0, 바위:1, 보:2 ::: '))
        computer_lose, computer_win, you_lose, you_win, same = rsp(you, cnt)#컴퓨터의 승패, 나의 승패, 무승부 수 반환값 받기
        cnt = cnt + 1
        games = games - 1
    print('\n')
    print(f'나의 전적: {you_win}승 {same}무 {you_lose}패')
    print(f'컴퓨터의 전적: {computer_win}승 {same}무 {computer_lose}패')

games = int(input("몇 판을 진행하시겠습니까? : "))
rsp_advanced(games)