f = open('test.txt', 'a', encoding='utf-8')

for i in range(5,9) :
    data = '%d번째 줄 입니다. \n' %i
    f.write(data)
f.close()