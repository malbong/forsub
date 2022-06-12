# keypoint
# 1) continue 
# 2) logic think
# 3) % 연산

i = 0
hap = 0
num_list = []

while i < 101:
    i += 1
    if i % 2 != 0:
        continue
    num_list.append(i)
    hap += i

print('짝수는', num_list)
print('짝수들의 합은', hap)
    
# while문 안에 if문이 관건
# 만약 if 문이 없으면 
# 1) num_list.append(i)가 짝홀수 구분없이 들어갈 것
# 2) 마찬가지로 hap += i 도 짝홀수 구분없이 들어갈 것
# 
# while i < 101:
#     i += 1
#     if i % 2 == 0:
#         num_list.append(i)
#         hap += i
# 이러한 코드가 더 아름다우나
# 시험에서 논리사고를 위해 코드를 꼬아 놈
# num_list.append(i)
# hap += i 를 짝수만 들어가게 하기 위해선
# if문에 홀수를 걸러야 함