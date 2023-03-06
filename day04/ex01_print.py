# 아래 두 개 는 똑같이 출력됨
print('pythone' 'javascript' 'java')
print('pythone'+'javascript'+'java')
# 문자열 사이에 ,(쉼표)로 작성 시 띄어쓰기가 됨
print('pythone','javascript','java')

# print 함수 호출 시, end매개변수에 끝문자를 지정할 수 있음
# 지정하지 않으면 자동으로 \n (줄바꿈)이 지정되어 있음
print(1, end= '')
print(2)

for i in range(5) :
    print(i, end= '')