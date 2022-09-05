def solution(new_id):
    answer = ''
    new_id = new_id.lower()

    l = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    new_id = ''.join(x for x in new_id if x in l)

    while new_id.count('..') >= 1:
        new_id = new_id.replace('..','.')

    new_id = new_id.strip('.')

    if not new_id:
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[14]=='.':
            new_id = new_id.rstrip('.')

    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    answer = new_id

    return answer

# new_id = input()
#
# print(solution(new_id))