# 쓰기 모드
f = open('test.txt', 'w', encoding='utf-8')
# f.write('집 가고 싶다..')
stu = ['이나영', '김아랑', '강하늘', '김우리']
score = [98,80,77,65]

for i in range(4) :
    data = '%s님은 %s점 입니다. \n' %(stu[i], score[i])
    f.write(data)
f.close()

# 읽기 모드
d = open('test.txt', 'r', encoding='utf-8')
readData = d.readlines()
for i in readData :
    print(i)
d.close()