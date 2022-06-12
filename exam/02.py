# 튜플 tuple
# list와 동일하나 값이 설정되고
# 수정할 수 없는 immutable list라고 생각하면 됨

# for x in list의list인 경우
# x가 list안쪽의 list를 받아옴
# ex) 
#  listOfList = [[1,2,3], [4,5,6]]
#  for x in listOfList:
#  x는 [1,2,3]받은 후에 다음 루프에 [4,5,6] 받음
#  cf) 받은 x를 다시 for문으로 받을 수도 있음
# ex)
# for x in listOfList:
#     for y in x:

# 찾을데이터 in 데이터집합
# 찾을데이터를 데이터집합에서 찾음
# -> 없으면 거짓, 있으면 참
# -> if문과 연결해서 사용

member = (('choi', 93), ('han', 50), ('jung', 92), ('kang', 68), ('kim', 80), ('lee', 90), ('moon', 65), ('na', 100), ('park', 75), ('song', 75))

search = input('검색할 아이디 입력 : ')

idList = []
for x in member:
    idList.append(x[0])

if search in idList:
    print('가입한 회원입니다.')
else:
    print('회원이 아닙니다.')