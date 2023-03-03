# while 조건문 :
#   실행문;

treeHit = 0
while treeHit < 10 :
    print('나무를 %d번 찍었습니다.' %treeHit)
    treeHit += 1
    
# number = 0
# while number != 4 :
#     print('4가 아닙니다.')
#     number = int(input())
    
fruits = ['사과' '오렌지']
fruits.append('딸기')
fruits.insert(1, '수박')
print(fruits)

# while문 사용해 1~10까지 숫자 중 홀수만 리스트에 넣어서 출력
numlist = []
num = 1
while num <= 10 :
    if(num % 2 == 1) :
        numlist.append(num)
    num += 1
print(numlist)