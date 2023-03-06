# 내장함수들

# abs(x) : 절대값을 반환
result1 = abs(-100)
print(result1)

# all(x) : 리스트, 듀플, 문자열 전체가 True일 때만 True리턴 나머지는 False
# any(x) : 하나라도 True면 True리턴
print(all(['', 20, '하하']))
print(all([[1,2], 20, '하하']))

print(any(['', 0, '']))
print(any(['', 0, [1,2]]))

# divmod(a, b) : a를 b로 나눈 몫과 나머지를 듀플로 반환
print(divmod(10, 3))

# enumerate() : (열거하다.) for문과 같이 쓸 경우, 인덱스와 value값을 같이 받을 수 있다 
list = ['a','b','c','d','e']
for i in range(len(list)) :
    print(i, list[i])
    
for i, v in enumerate(list) :
    print(i, v)
    
# max() : 최댓값 반환
print(max([80,90,60,70,50]))

# min() : 최솟값 반환
print(min([10,20,50,40,30]))

scores = [10,20,30,60,25,90]
maxscore = max(scores)
maxindex = scores.index(maxscore)
print('최대값은 %d이고, %d번째 값이다.' %(maxscore, maxindex))

# round() : 반올림해서 반환
print(round(12.6789, 2))

# sum(x) : 리스트나 듀플을 입력받아 모든 요소의 합을 반환
numTuple = (2,3,4,5,6)
print(sum(numTuple))