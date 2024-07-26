# 연산자

a = 4
b = 2

# 산술 연산자
print(a+b)
print(a-b)
print(a*b)
print(type(a/b)) # 나누기는 값과 상관없이 float로 반환함

# 몫/ 나머지/ 제곱 -> 몫과 나머지는 모두 정수의 형태! // float를 나누는 경우, 몫과 나머지는 float의 형태가 됨
print(type(a//b)) # int
print(type(a%b)) # int
print(type(a**b)) # int

# 복합 연산자
c = 2
d = 3
c += d
print(c)

# 비교 연산자 >, <, >=, <=, ==, !=
a = 'a'
b = 'b'
print(a == b) # 알파벳에도 순서가 있어서 비교 가능함(문자열 간 비교는 가능, abcd 뒤로 갈수록 크다고 여김) / 문자와 숫자 간 비교는 불가

# 논리 연산자 (and, or, not)
a = 20>10 #True
b = 'hello' == 'Hello' #False
print(a and b)
print(a or b)

a = '  ' # true
print(not a)