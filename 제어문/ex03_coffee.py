coffiee = 10
while True :
    money = int(input('돈을 넣어주세요 : '))
    if money == 300 :
        print('커피 받으세요~')
        coffiee = coffiee - 1
    elif money > 300 :
        print('거스름돈 %d를 주고, 커피 받으세요~' %(money - 300))
        coffiee = coffiee - 1
    else :
        print('돈이 부족합니다 고객님..^^')
    if coffiee == 0 :
        print('오늘 준비한 커피가 모두 소진되었습니다..ㅠ [영업 종료]')
        break