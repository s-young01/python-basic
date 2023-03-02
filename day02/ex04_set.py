# 집합 자료형 (파이썬 2.3부터 지원)
# 중복 허용하지 않음, 순서가 없다(인덱싱으로 값을 얻을 수 없음)

s1 = set([1,2,3,4,5])
s2 = set('hello')
print(s1)
print(s2)

# 인덱스 값으로 접근하고 싶을 때는 리스트로 변환해서 접근
l2 =  list(s2)
print(l2[1])

# 중복 제거 하고 싶을 때 (리스트로 변환)
s3 = set([1,2,3,4,1,2,4])
print(s3)
l3 = list(s3)
print(l3)

# 집합 관련 함수
# 교집합
numberset1 = set([1,2,3,4,5,6])
numberset2 = set([4,5,6,7,8,9])
print(numberset1 & numberset2)
print(numberset1.intersection(numberset2))

# 합집합
print(numberset1 | numberset2)
print(numberset1.union(numberset2))

# 차집합
print(numberset1 - numberset2)
print(numberset1.difference(numberset2))

# 값 한 개 추가하기
numberset1.add(20)
print(numberset1)

# 값 여러 개 추가하기
numberset1.update([100, 200, 300])
print(numberset1)

# 특정 값 제거하기 
numberset1.remove(100)
print(numberset1)