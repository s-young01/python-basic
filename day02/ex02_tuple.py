# 듀플은 요소값 수정, 삭제 못함
t1 = (1,2,3)
print(t1)
t2 = (1,)
print(t2)
t3 = 1,2,3
print(type(t3))

# 듀플에 요소 변경이나 삭제하면 오류
# t3[0] = 10
# del t3[0]
# print(t3)

# 듀플 다루기 인덱싱, 슬라이싱, +, *, 길이 구하기(len())
print(t3[0:2])

print(t1 + t3)
print(t1 * 3)
print(len(t1))