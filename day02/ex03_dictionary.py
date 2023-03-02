# 딕셔너리 자료형 {key: value} 형태
# key를 통해 value에 접근한다 (key는 중복 불가)

dic1 = {'name' : 'green', 'phone' : '01012345678', 'age' : 30}
dic2 = {1 : 'a', 2 : 'b', 3 : 'c'}

# 속성 추가하기
dic1['isJob'] = True
print(dic1)

dic2[4] = 'd'
print(dic2)

# value값 접근하기
print(dic1['name'])

# 요소 삭제하기
del dic1['phone']
print(dic1)

# key값이 중복될 시 맨 뒤에 있던 key값으로 덮어 씌워짐
dic3 = {'name' : 'blue', 'age' : 20, 'name' : 'pink'}
print(dic3)

# key 리스트 만들기
dic3key = dic3.keys()
print(dic3key)
# 리스트 타입으로 형 변환 list()
dic3keyList = list(dic3key)
print(dic3keyList)

# value 리스트 만들기
dic3value = dic3.values()
print(dic3value)
# 리스트 타입으로 형 변환 list()
dic3valueList = list(dic3value)
print(dic3valueList)

# key, value쌍 얻기 
dic3item = dic3.items()
print(dic3item)
# 리스트 타입으로 형 변환 list()
dic3itemList = list(dic3item)
print(dic3itemList)

# key, value쌍 모두 지우기
dic3.clear()
print(dic3)

# key로 value값 얻기
dic4 = {'name' : '구름', 'age' : 3, 'color' : 'white'}
print(dic4.get('name'))
print(dic4.get('age'))
# 없는 key로 접근 했을 때 (None을 반환)
print(dic4.get('play'))
# 디폴트 지정하기 get(key, default값)
print(dic4.get('play', 'cool'))
# 대괄호 표기법으로 없는 key로 접근 했을 때 (오류)
# print(dic4['play'])

# 해당 key값 있는지 확인
print('name' in dic4)
print('play' in dic4)