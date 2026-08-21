# 반복문 while 조건: 조건이 참인 동안 블록수행
a = 1 # 조건의 초기치
while a<= 5:  #조건                      조건이 거짓이 될 때 까지 무한루프
    print(a, end = '')
    a +=1  # 조건의 증가치
# else: # 선택적: 정상 조건에 따른 종료시 수행
#     print('수행성공')

print()
i=1
while i <= 3:
    j=1
    while j<=4:
        #print('i='+str(i)+',j='+str(j)) #밑과 같은내용        int(1)=숫자, str(1)=문자
        print(f'i={i},j={j}')
        j= j + 1
    i = i + 1

print('1 ~ 100 사이의 정수 중 3의 배수의 합은?')
su = 1
hap = 0
while su <= 100:
    #print(su, end = '') # end = ''은 옆으로 찍음 
    if su % 3 == 0:
        #print(su, end = '')
        hap += su
    su += 1

print('합은', hap)


print()
colors = ['r', 'g', 'b']
num = 0
while num < len(colors):
    print(colors[num])
    num += 1

print('if블럭내에 while문을 사용')
import time
# print('a')
# time.sleep(2)
# print('b')

# sw = input('폭탄스위치를 누를까요?[y/n]')

# if sw == 'Y' or sw == 'y': 
#     count = 5
#     while 1<= count:
#         print('%d초 남았어요'%count)
#         #print(f'{count}초 남았어요) #위와 같다
#         time.sleep(1)
#         count -= 1
#     print('폭발')
# elif sw == 'N' or sw == "n":
#     print('작업취소')

# else:
#     print('y 또는 n을 누르시오')

print('\ncontinue / break')
a = 0
while a < 10:
    a += 1
    if a == 7: break # 반복문 무조건 탈출
    if a == 5: continue # 아래문을 무시하고 while로 이동
    print(a)
else:       # 선택적 : 조건에 따른 종료 시 수행
    print('수행성공') 

print('\n키보드로 점수를 입력받아 홀수, 짝수 출력(무한반복)')
while True:
    mysu = int(input('확인할 정수 입력(예:5)'))
    if mysu == 0:
        print('프로그램 종료')
        break
    elif mysu % 2 == 0:
        print(f'{mysu}:짝수')
        continue
    elif mysu % 2 == 1:
        print(f'{mysu}:홀수')


print('끝')








