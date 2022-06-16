# keypoint
# 1) if문을 잘 이해하는가?
# 2) list의 index를 잘 이해하는가?

# 실행 절차 잘 보기
# list[-1] -> 맨끝에 값을 반환
# index -> [ 0,  1,  2,  3,  4,  5]
# index -> [-6, -5, -4, -3, -2, -1]

# lists = ["abc", "def", ["xyz"]]
# lists[0] -> abc
# lists[0][1] -> b
# lists[1][2] -> f
# lists[2][0][1] -> y

friend_list = []
word_list = []
count = 1
index = 0

friend = input("이름을 입력하시오(건국이): ")
word = input("단어를 입력하시오(apple): ")

while True:
    friends = input("이름을 입력하시오(건식이): ")
    friend_list.append(friends)
    words = input("단어를 입력하시오(elephant): ")
    word_list.append(words)

    if count == 1:
        if word[-1] == words[0]:
            print("끝말잇기 성공")
        else:
            print(friends, "님", "끝말잇기 실패. 다음번에 커피사세요.")
            break
    else:
        if word_list[index][-1] == words[0]:
            print('끝말잇기 성공')
        else:
            print(friends, "님", "끝말잇기 실패. 다음번에 커피사세요.")
            break
        index = index + 1
    
    count = count + 1
