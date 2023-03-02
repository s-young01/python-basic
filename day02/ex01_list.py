list1 = ["a","b","c","d"]
print(list1)
print(type(list1))
print(list1[0])

# 리스트의 슬라이싱 [start:end] end번째는 포함하지 않음
print(list1[0:3])
list2 = [1,2,3]
list3 = [4,5,6]

# 리스트 더하기 + 기호를 사용하면 리스트 합쳐준다
list4 = list2 + list3
print(list4)

# 리스트 반복하기 * 기호를 사용하면 리스트를 반복해 새로운 리스트를 반환
list5 = list2 * 3
print(list5)

# 리스트 길이구하기 len(리스트)
print(len(list5))

# 리스트 수정, 삭제 (del 객체)
list2[0] = 10
print(list2)
del list2[0]
print(list2)
del list5[4:]
print(list5)

students = ["stu1","stu2","stu3","stu4"]
# 리스트에 요소 추가 append()
students.append("stu5")
print(students)

# 리스트에 요소 추가(원하는 위치) insert(start,value)
students.insert(1, "newStu")
print(students)

# 리스트 뒤집기 reverse()
students.reverse()
print(students)

# 리스트 정렬 sort()
students.sort()
print(students)

numderList = [5,2,1,6,7,8,2,10]
numderList.sort()
print(numderList)

# 인덱스 반환 index(value)
num1 = students.index("stu3")
print(num1)
# 없는 인덱스 찾을시 => 오류 발생
# num2 = students.index("stu10")
# print(num2)

# 리스트 요소 제거 remove(value)
students.remove("newStu")
print(students)

numderList.remove(2)
print(numderList)

# 리스트 마지막 요소 리턴 후 삭제 pop()
lastList =  students.pop()
print(lastList)
print(students)

# 리스트에 포함된 요소의 개수 세기 count(value)
fruits = ["사과","딸기","사과","바나나","사과", "귤"]
applenum =  fruits.count("사과")
print(applenum)