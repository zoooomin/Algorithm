guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333
유미,123-1234-1234"""

def wrong_guest_book(guest_book):
    fw = open('guest_list.txt','w')
    fw.write(guest_book)
    fw.close()

    fr = open('guest_list.txt','r')
    wrong_list = []
    for i in fr:
        i = i.rstrip()
        # wrong1 :010 으로 시작하지 않는 번호
        # wrong2 :번호가 - 로 구분이 되어 있음->'-'가 2개여야 함
        # wrong3 :-를 포함하여 길이가 13이 아닌 경우
        wrong1 = i[i.find(',')+1:i.find('-')] != '010'
        wrong2 = i.count('-') != 2
        wrong3 = len(i[i.find(',')+1:]) != 13

        if wrong1 or wrong2 or wrong3:
            wrong_list.append(i)

    for name_num in wrong_list:
        find_comma = name_num.find(',')
        print('잘못 쓴 사람:', name_num[:find_comma])
        print('잘못 쓴 번호:', name_num[find_comma+1:])
        print('\n')

wrong_guest_book(guest_book)