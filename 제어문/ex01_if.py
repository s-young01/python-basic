# if 조건문 :
#   수행 구문
# else :
#   수행 구문

money = 5000

if money > 10000 :
    print('택시 타고 감')
else :
    print('걸어 감')
   
# 비교 연산자 
print(10 == 20)
print(10 != 20)

money2 = 2000
card = True

if money2 > 3000 or card:
    print('택시 타고 감')
else :
    print('걸어 감')
    
if not card :
    print('카드가 없다')
else :
    print('카드가 있다')
    
# score 값을 입력
# 91 ~ 100 = "A"
# 81 ~ 90 = "B"
# 71 ~ 80 = "C"
# 70 이하 = "D"
score = int(input('점수를 입력하세요 : '))
if score >= 91 :
    print('A')
elif score >= 81 :
    print('B')
elif score >= 71 :
    print('C')
else :
    print('D')
    
# 숫자를 입력 받은 후 홀수인지 짝수인지 출력
num = int(input('숫자를 입력하세요 : '))
if num % 2 == 0 :
    print('짝수입니다.')
else :
    print('홀수입니다.')
    
# 조건부 표현식
# 참인 경우 할당할 값 if 조건문 else 거짓인 경우 할당할 값
result = '짝수' if num % 2 == 0 else '홀수'
print(result)

# in / not in 리스트, 듀플, 문자열
# in은 있으면 True, not in은 없으면 True
print( 5 in [1,2,3,4,5]) # 있으니까 True
print( 5 not in [1,2,3,4,5]) # 있어서 False

pocket = ['paper','cellphone','card']
if 'money' in pocket :
    print('택시 타고 감')
elif 'card' in pocket :
    print('카드로 버스 타고 감')
else :
    print('걸어 감')
    
# useId -> 아이디 입력, userPw -> 패스워드 입력
# 'green', '1234' 로그인 되었습니다 출력
# 'green'이 아닐 경우, 아이디가 틀렸습니다 출력
# '1234'가 아닐 경우, 비밀번호가 틀렸습니다 출력

userId = input('아이디를 입력하세요')
userPw = input('비밀번호를 입력하세요')
if userId == 'green' :
    if userPw == '1234' :
        print('로그인 되었습니다.')
    else :
        print('비밀번호가 틀렸습니다.')
else :
    print('아이디가 틀렸습니다.')
    
# 조건부 표현식으로 바꾸기
if userId == 'green' and userPw == '1234' :
    print('로그인 되었습니다.')
elif userId == 'green' :
    print('비밀번호가 틀렸습니다')
elif userPw == '1234' :
    print('아이디가 틀렸습니다')
else :
    print('둘 다 틀렸습니다')