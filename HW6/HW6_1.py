# dict = { key1:value1, key2:value2, key3:value3 }
# print(dict[key1])
# -> value1
# print(dict[key2])
# -> value2

# print(딕셔너리변수.items()) 해볼 것
# ex) dict1 = {'김말봉':22, '홍길동':25 }
# print(dict1)
# print(dict2)

# for문에 그냥 dictionary 넣으면 key를 하나씩 넘겨줌
# for key in dict:
#     print(key)

# for문에 dict.items()함수를 호출하면 (key, value) 쌍을 넘겨줌
# 그것을 두가지 변수로 받는 것
# for key, value in dict.items():
#     print(key, value)

# "문자열 {} {} {}".format(data1, data2, data3)
# -> {}에 순서대로 data1~3까지 들어감

price = {"어묵":"500원", "떡볶이":"300원", "라면":"3000원"}
# 1
for i in price:
    print("{}:{}".format(i, price[i]))

# 2
for key, value in price.items():
    print("{}:{}".format(key, value))