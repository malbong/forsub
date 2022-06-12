# 빈 리스트 작성법
# 1) 리스트변수 = list()
# 2) 리스트변수 = []

# 리스트에 데이터 추가하기
# 리스트변수.append(데이터)

# 입력받기
# input("메시지")
# -> input() 함수는 데이터를 문자열로 받으므로
# -> int()함수로 정수로 변환할 필요가 있음

# sum() 함수 알아보기
# 1) sum([1,2,3,4]) 
#    -> 10
# 2) list1 = [1,2,3,4]
#    sum(list1) 
#    -> 10


scores = list()
for i in range(5):
    scores.append(int(input("점수를 입력하세요:")))
print(scores)
print("입력받은 프로그래밍을 통한 문제해결 과목 5명의 평균은 {}입니다".format(int(sum(scores) / 5)))
