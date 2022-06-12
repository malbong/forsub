# keypoint
# 1) import문으로 사용할 수 있는가
#  1-1) random으로 난수를 만들 수 있는가
# 2) 구현을 잘 할 수 있는가
# 3) 함수를 이해하는가
#  3-1) 지역변수와 전역변수의 이해 

# import로 외부 라이브러리(함수들)를 가져 올 수 있음
# random.randInt(start, end)
# -> start <= N < end

# 지역변수
# 해당 스코프에서만 사용가능한 변수
# 전역변수
# 어디서든 사용할 수 있는 변수
# -> 상당한 어려운 내용
# 일단 외부의 변수를 사용하고 싶으면 global로 선언하여 사용
# 그럼 해당 변수가 전역변수가 됨

# 00) 에러 아님 -> a가 함수실행전 선언되었기 때문
# def func():
#     print(a)
# a = 1 # 전역변수
# func()
# print(a)

# 01) 에러 -> 함수 실행전 a가 선언되었기 때문
# def func():
#     print(a)
# func()
# a = 1
# print(a)

# 02) 에러 아님 (중요)
# -> a가 밖에서 전역으로 1로 선언했지만
# -> func()함수에서 a = 3으로 할당함
# -> 밖의 a와 func()안의 a는 다른 변수임 (전역변수와 지역변수)
# def func():
#     a = 3 # 지역변수 a 새로 선언한 것 (밖의 a와 다름)
#     print(a) # 3 출력
# a = 1 # 전역변수
# func()
# print(a) # 1 출력

# 03) 에러 (중요)
# -> a가 밖에서 전역으로 1로 선언했지만
# -> 밖의 a와 func()안의 a는 다른 변수임 (전역변수와 지역변수)
# -> 전역, 지역변수와 관련없이
# -> 함수 내부에서 a를 값을 초기화 하지 않았는데 증가식을 사용하므로 에러임    
# def func():
#     a += 1 # 지역변수 a를 초기화 하지 않아서 에러인 것
# a = 1
# func()
# print(a) 

# 04) 에러 아님 (중요)
# -> a를 global로 선언해서 전역변수로 사용하기 때문
# -> func()에서 지역변수 a가 아닌 전역변수 a를 사용한다고 했으므로
# -> func()밖의 전역변수인 a를 사용하는 것
# def func():
#     global a
#     a += 1
# a = 1
# func()
# print(a) # 2 출력

import random

def diceGame():
    global user_cnt
    global com_cnt
    global same_cnt

    user = random.randint(1, 6)
    com = random.randint(1, 6)
    print("당신: {}, 컴퓨터: {}".format(user, com))

    if user > com:
        print("당신이 이겼습니다.\n")
        user_cnt += 1
    elif user < com:
        print("당신이 졌습니다.\n")
        com_cnt += 1
    else:
        print("비겼습니다.\n")
        same_cnt += 1

num = int(input("게임을 몇 번 할까요? "))
print()

user_cnt = 0
com_cnt = 0
same_cnt = 0

for i in range(num):
    diceGame()

print("게임 결과는 {}전, {}승, {}무, {}패입니다.".format(num, user_cnt, same_cnt, com_cnt))