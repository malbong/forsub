# ========================================================
# 간단하지만 반복문 or 함수들을 사용하지 않은 경우
sub1 = int(input('1st: '))
sub2 = int(input('2nd: '))
sub3 = int(input('3rd: '))
sub4 = int(input('4th: '))
avg = (sub1 + sub2 + sub3 + sub4) / 4

if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and sub4 >= 40 and avg >= 60:
    print('합격')
else:
    print('불합격')



# ========================================================
# 리스트를 배운경우
# subs = [];
# subs.append(int(input('1st: ')))
# subs.append(int(input('2nd: ')))
# subs.append(int(input('3rd: ')))
# subs.append(int(input('4th: ')))
# for score in subs:
#     if score < 40:
#         print('불합격')
#         exit()

# avg = sum(subs) / len(subs)
# if avg < 60:
#     print('불합격')
# else:
#     print('합격')

