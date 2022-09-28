#아나그램(리스트해쉬)
a = input()
b = input()
str1 = [0] * 52 #알파벳 소문자 대문자 26개씩
str2 = [0] * 52
for x in a:
    if x.isupper():
        str1[ord(x)-65] += 1 #대문자
    else:
        str1[ord(x)-71] += 1 #소문자
for x in b:
    if x.isupper():
        str2[ord(x)-65] += 1 #대문자
    else:
        str2[ord(x)-71] += 1 #소문자

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")


