print('파일 처리 : 입출력')
import os # 운영체제(os)와 관련된 기능 제공

try:
    print('파일읽기 ------')
    print(os.getcwd()) # c:\works\projects\pro2

    # 읽을 파일 c:\works\projects\pro2\ftest.txt
    # f1 = open(file=os.getcwd() + r'\ntest.txt', mode='r', encoding='utf-8')
    # f1 = open(r'C:\works\projects\pro2\ntest.txt', mode='r', encoding='utf-8')
    f1 = open(r'ftest.txt', mode='r', encoding='utf-8') #권장
    print(f1)
    print(f1.read())
    f1.close

    print('\n파일저장-----')
    f2 = open('ftest2.txt', mode='w', encoding='ufs-8')
    f2.write('내 친구들\n')
    f2.write('신기해, 이기자\n')
    f2.close()
    print('파일내용 저장성공')

    print('\n파일내용추가-----')
    f3 = open('ftest2.txt', mode='a', encoding='ufs-8')
    f3.write('\n사오정')
    f3.write('\n손오공')
    f3.write('\n저팔계')
    f3.close()
    print('파일내용 추가 성공')

    #ftest2.txt 읽기
    print('~~~~~~~~~~~~~~~~~~')
    print()
    f4 = open('ftest2.txt', mode='r', encoding='ufs-8')
    print(f4.read())
    f4.close()

except Exception as e:
    print("처리오류:", e)

