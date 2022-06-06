# 과제는 직접 해보기


# list는 +로 뒤에 append 가능 
# list1 = [1, 2, 3]
# list2 = [4, 5]
# list3 = list1 + list2
# list3 == [1, 2, 3, 4, 5]임

# list4 = [4, 5] + [1, 2, 3]
# list4 = [4, 5, 1, 2, 3]임

# list5 = [0] + [0]
# list5 = [0, 0] 임


# list끼리의 비교가능
# 각 list의 처음부터 비교함
# 만약 아래의 리스트가 존재한다하면
# list1 = [1, 2, 3]
# list2 = [1, 2, 4]
# 첫번째의 값은 동일하여 넘어감
# 두번째 값도 동일하여 넘어감
# 세번째 값은 list2가 4로 3보다 크므로 list2가 더 큰 리스트임
# print(list1 < list2) -> True

# list1 = [1, 999]
# list2 = [2]
# 첫번째 값이 1과 2의 비교이므로 list2가 더 큰 리스트임
# print(list1 < list2) -> True

# list1 = [1, 2, -999]
# list2 = [1, 2]
# 첫번째 값, 두번째 값은 동일함
# 세번째 값은 list1에 존재하나 list2에 존재하지 않음
# 이전의 값들의 비교는 동일한데 list1가 더 기므로 list1가 큰 리스트임
# print(list1 < list2) -> False

# list1 = [1, 2]
# list2 = [2, 1]
# 언뜻보면 같으나 첫번째 값부터 비교하므로
# list2 가 더 큰 리스트가 됨
# print(list1 < list2) -> True

# 값도, 순서도, 길이도 같으면 같은 리스트
