#Chapter 2-2
#파이썬 변수

#기본 선언
n = 700 #정수를 알파벳 n에 담아두는 것. (할당)
#n이라는 주소를 할당해 정수 700을 저장한다.

print(n) #n이라는 주소에 접근해 700이라는 값을 받는다.
print(n * 700)  #n에 저장된 값에 700을 곱해서 출력한다.
print(type(n))  #n의 자료형을 보여준다.

#동시 선언
x = y = z = 700
print(x, y, z)

#선언
var = 75

#재선언
var = "Change Value"

print(var)          #Change Value
print(type(var))    #<class 'int'>

# Object Reference
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))

# 예2)
# n -> 777
n = 777

print(n, type(n))
print()

m = n
#m = 777 과 같다.
print(m, n)
print(type(m), type(n))

n = 400
print(m, n)
print(type(m), type(n))

# id(identity)확인 : 객체의 고유값 확인
m = 800
n = 655
print(id(m))
print(id(n))
print()

# 같은 오브젝트 참조
n = 800
print(id(m))
print()

# 다양한 변수 선언 방법
#camelCase -> 메소드
#PascalCase -> 클래스
#snake_case -> 변수

#허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age = 7
age_ = 8
_AGE_ = 9

#예약어(reserved word)는 사용이 불가능하다.