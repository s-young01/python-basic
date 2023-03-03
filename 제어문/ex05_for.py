list1 = ['one','two','three']
for i in list1 :
    print(i)
    
for i in "green" :
    print(i)
    
marks =[90,50,67,70,80]
number = 0
for stu in marks :
    number += 1
    if stu >= 70 :
        print('%d번 학생은 합격입니다.' %number)
    else :
        print('%d번 학생은 불합격입니다.' %number)
        
print(list(range(1, 10, 2)))
# range()함수 사용하기

sum = 0
for i in range(1, 11) :
    sum = sum + i
print('1 ~ 10까지 더한 수는 %d 이다.' %sum)

sum1 = 0
for i in range(1, 11, 2) :
    sum1 = sum1 + i
print('1 ~ 10까지 숫자 중 홀수만 더한 수는 %d 이다.' %sum1)

# for와 range()함수 사용해 구구단 출력하기
for i in range(2, 10) :
    for j in range(1, 10) :
        print('%d * %d = %d' %(i, j, i * j))