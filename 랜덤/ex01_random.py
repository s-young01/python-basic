# import 모듈 불러오기
import random

# random() : 0.0 ~ 1.0 사이의 난수 값을 반환
num = random.random()
print(num)

# randint(start, end) : start ~ end 사이의 정수 랜덤 값을 반환
num2 = random.randint(1, 5)
print(num2)

# 01. 평균 구하기
# [70,60,55,75,95,90,80,85,100] 리스트를 
# for문을 사용하여 A학급의 평균 점수를 출력
Test_List = [70,60,55,75,95,90,80,85,100]
listSum = 0
for i in Test_List :
    listSum += i
    ave = listSum / len(Test_List)
print('A학급의 평균 점수는 %d점 입니다.' %ave)

# 02. * 출력 (1 ~ 5까지)
star = 1
while star < 6 :
    print('*' * star)
    star += 1

# 03. 가위바위보 게임 만들기
# 가위, 바위, 보 중 하나를 입력받고, 컴퓨터는 랜덤으로 가위, 바위, 보 중
# 하나를 지정하고 사용자와 컴퓨터 중 누가 이겼는지 출력
rps = input('가위, 바위, 보 중 하나를 입력하세요 : ')
comrps = ''
if rps != '가위' and rps != '바위' and rps != '보' :
    print('잘못 입력하셨습니다.')
else :
    print('사용자는 %s를 냈습니다.' %rps)
    rpsnum = random.randint(1, 3)
    comrps = '가위' if rpsnum == 1 else '바위' if rpsnum == 2 else '보'
    print('컴퓨터는 %s를 냈습니다.' %comrps)
    if rps == comrps :
        print('비겼습니다.')
    elif (rps == '가위' and comrps == '보' or
          rps == '바위' and comrps == '가위' or 
          rps == '보' and comrps == '바위') :
        print('사용자가 이겼습니다.')
    else :
        print('컴퓨터가 이겼습니다.')
        
# 04. 로또번호 출력하기
# 1 ~ 45 까지 중복되지 않는 랜덤한 숫자로 6개 출력
# 두 개의 리스트 생성 lottolist = [] / resultlist = []
lottolist = []
resultlist = []

for i in range(1, 46) :
    lottolist.append(i)
for i in range(6) :
    # 1 ~ 45 가 담겨진 lottolist의 index번호는 0 ~ 44
    randomNum =  random.randint(1, len(lottolist) - 1)
    lotto = lottolist.pop(randomNum)
    resultlist.append(lotto)
print(resultlist)