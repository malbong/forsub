# HW6_01.py 참고

singer = dict()

print("요즘 가장 핫한 아이돌이라죠. 소개합니다!!")
singer["그룹이름"] = "에스파"
singer["구성원수"] = "4명"
singer["대표곡"] = "Next Level"

for i,j in singer.items():
    print("[{}:{}]".format(i,j), end=" ")