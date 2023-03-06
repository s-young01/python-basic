# 다음과 같은 내용을 지닌 test2.txt 파일이 있다,
# 이 파일의 내용 중 java라는 문자열을 python으로 변경해서 저장하시오
# Life is too short
# you need java

f = open('test2.txt', 'r')
# 파일 내용을 body변수에 저장
body = (f.read()) 
f.close()

# 문자열 변경
body = body.replace('java', 'python') 
# 파일을 쓰기 모드로 실행
f = open('test2.txt', 'w', encoding='utf-8')
f.write(body)
f.close()