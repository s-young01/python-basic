# 문자열 인덱싱문제 

# 01. pin = "881120-16068234" 성별을 나타내는 숫자를 출력하세요.
pin = "881120-16068234"
print(pin[7])

# 02. 문자열 "a:b:c:d"가 있다 replace를 사용해 "a#b#c#d"로 바꿔서 출력하세요.
a = "a:b:c:d"
b = (a.replace(":", "#"))
print(b)

# 03. [1,3,5,4,2] 리스트를 [5,4,3,2,1]로 출력하세요.
list1 = [1,3,5,4,2]
list1.sort()
print(list1.reverse())

# 04. ["life", "is", "too", "short"] 리스트를 문자열로 만들어서 출력하세요.
list2 = ["life", "is", "too", "short"]
result = (" ".join(list2))
print(result)

# 05. [1,1,1,2,2,2,3,3,4,4,5,5,6] 리스트를 중복 제거하고 출력하세요.
liset1 = set([1,1,1,2,2,2,3,3,4,4,5,5,6])
li2 = list(liset1)
print(li2)