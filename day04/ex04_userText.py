f = open('userText.txt', 'w', encoding='utf-8')
f.close()
while True :
    f = open('userText.txt', 'a', encoding='utf-8')
    userText = input('적고 싶은 내용을 작성해 주세요(stop을 누르면 종료합니다)')
    if userText == 'stop' : break
    f.write(userText + '\n')
f.close()