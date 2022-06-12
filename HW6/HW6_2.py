# 직접해보기
# 중첩 반복
# 안쪽이 다 반복해야 바깥쪽이 다음 루프 실행

for i in range(1, 4):
    for j in range(1, 4):
        print(i, "*", j, "=", i * j)
    print("============")