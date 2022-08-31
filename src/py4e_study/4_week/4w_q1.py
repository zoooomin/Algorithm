# Q1. 숫자를 입력받고 3자리마다 찍기(함수 이용)
def make_comma(num):
    num = num[::-1]
    n_num = ''
    num_len = len(num)
    for i in range(0, num_len, 3):
        n_num = n_num + num[i:i+3] + ' '
    n_num = n_num[::-1].lstrip().replace(' ',',')
    print(n_num)

num = input('enter the number: ')
make_comma(num)