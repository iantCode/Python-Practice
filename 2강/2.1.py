#Print 사용법

#기본 출력
import sys  # sys.stdout는 콘솔에 출력하기 위해 사용함. 나중에 텍스트 파일에 프린트할 수 있기도 한다.
print('Python Start!')  # () 내부는 파라미터라고 부름. 보통 '', ""를 사용한다
print("Python Start!")
print('''Python Start!''')  # ''' 또는 """도 사용할 수 있기는 하지만 보통 사용하지는 않는다.
print("""Python Start!""")

print()  # print 함수는 자동으로 줄바꿈을 한다.

#Seperator 옵션
# sep 파라미터는 ,로 분리된 곳 사이에 어떻게 할 지 나타낸다.
print('P', 'y', 't', 'h', 'o', 'n', sep="")
print('010', '1234', '1234', sep='-')
print('python', 'google.com', sep='@')

print()

#End 옵션

print('Welcome to ', end='')  # print 함수는 자동으로 줄바꿈을 하지만 end 옵션이 있다면 이대로 처리한다.
print('My Server ', end='')
print('Web Site')
print()

#file 옵션

print('Learn Python', file=sys.stdout)
print()

#format 사용 (d, s, f)
print('%s %s' % ('one', 'two'))  # 정석적이다.
print('{} {}'.format('one', 'two'))  # 유연하게 사용할 수 있다.
print('{1} {0}'.format('one', 'two'))  #format의 파라미터의 1번째는 0번으로 처리된다.
print()

#현재 계속 학습 중