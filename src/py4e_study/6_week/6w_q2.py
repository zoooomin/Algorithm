# 이름, 실적
member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2],
           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]

def sales_management(member_names, member_records):
    member = dict()
    for i in range(6):
        avg = round(sum(member_records[i])/len(member_records[i]), 2) #멤버 별 실적에 대한 평균
        member[member_names[i]] = avg #딕셔너리 만들기

    member_li = sorted([(v, k) for k,v in member.items()], reverse=True) #튜플로 변환하여 값을 정렬할 수 있게함

    bonus_member(member_li[:2]) #1,2등
    ftof_member(member_li[-2:]) #5,6등

def bonus_member(member):
    '''보너스 대상자 판별 : 실적 5보다 커야함'''
    bonus_mem = dict(member)
    for k in bonus_mem:
        if k > 5:
            print('보너스 대상자 ', bonus_mem.get(k))
        else:
            continue

def ftof_member(member):
    '''면담 대상자 판별 : 실적 3보다 작아야함'''
    ftof_mem = dict(member)
    for k in ftof_mem:
        if k < 3:
            print('면담 대상자 ', ftof_mem.get(k))

sales_management(member_names, member_records)