# 함수 입력값 ==> 함수 ==> 리턴값

# 1. 일반적인 함수 : 입력값과 리턴값이 있는 함수
def add(a, b) :
    # 리턴문은 함수 실행 즉시 종료
    return a + b 

re = add(1, 3)
print(re)

# 2. 입력값이 없는 함수
def printHi() :
    print('안녕')
    
printHi()

# 3. 매개변수 지정해서 호출하기 
# 매개변수를 지정해서 호출하면 순서 상관없이 사용할 수 있음
def sub(a, b) :
    return a - b

re2 = sub(b=10, a=20)
print(re2)

# 4. 입력값이 몇 개가 될지 모를 때 *매개변수
# *매개변수 : 입력값을 전부 모아서 듀플로 만들어줌 !
def addMany(*args) :
    result = 0
    for i in args :
        result = result + i
    return result

re3 = addMany(1,2,3,4,5)
re4 = addMany(2,3,4)
print(re3)
print(re4)

# 매개변수에 초기값 설정하기
def sayMy(name, age, man = True) :
    print('나의 이름은 %s입니다.' %name)
    print('나의 나이는 %d살 입니다.' %age)
    if man :
        print('남자입니다.')
    else :
        print('여자입니다.')
        
sayMy('김그린', 22)
sayMy('이블루', 30, False)