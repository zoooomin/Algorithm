# 6명의 회원이고 "아이디,나이,전화번호,성별,지역,구매횟수" 순서로 입력되어 있음
info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"
info_s = ['아이디', '나이', '전화번호', '성별', '지역', '구매횟수']
def good_customer(info):
    info_li = info.split(',')
    mem_li = list()
    tmp_li = list()
    cnt = 1
    for li in info_li:
        tmp_li.append(li)
        if cnt % 6 == 0:
            mem_li.append(tmp_li)
            tmp_li = []
        cnt += 1

    print_info(mem_li)
    get_cpn(mem_li)

def get_cpn(mem_li):
    '''쿠폰을 받을 수 잇는 멤버 구하기'''
    for mem in mem_li:
        if int(mem[5]) > 8 and (mem[2] != '010-0000-0000'):
            print(f'할인 쿠폰을 받을 회원정보 아이디:{mem[0]}, 나이: {mem[1]}, 전화번호: {mem[2]}, 성별: {mem[3]}, 지역: {mem[4]}, 구매횟수: {mem[5]}')

def print_info(mem_li):
    '''회원 정보 출력'''
    members = dict()
    for j in range(len(mem_li)):
        val = []
        for i in range(len(mem_li)):
            if mem_li[i][j] == 'x': #전화번호가 x인 회원은 010-0000-0000으로 바꿔서 출력
                mem_li[i][j] ='010-0000-0000'
            val.append(mem_li[i][j])
        members[info_s[j]] = val
    print(members)

good_customer(info)