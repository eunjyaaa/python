# for 반복문
# 반복 횟수가 정해져 있을 때!
# 반복 횟수 -> 컨테이너 원소의 갯수

# 리스트 활용 반복문
students = ['가나','다라','마바','사아'] # 리스트 (컨테이너)

for student in students:
    print(student + '님, 안녕하세요!')

print(student)

# 문자열 활용 반복문
sentence = '티모시 살라메는 잘생겼당'
print(len(sentence))
for char in sentence:
    print(char, end='!') # 한 단어씩 돌 때마다 뒤에 느낌표 붙여서 출력됨

# range 활용 반복문
for i in range(0,10,1):
    print(i)

# 리스트
grade = ['1학년', '3학년', '5학년']
names = ['가나','다라','마바']

print(len(grade))
print(range(len(grade)))

for i in range(len(grade)):
    print(grade[i]+names[i])
 
# for문으로 range를 활용하여 1~10 더한값 55 출력하기
result = 0
for i in range(1,11,1):
   result = result + i
print(result)

# for문과 조건문을 사용하여, 짝수인 경우만 더한 값을 출력하기
result_1 = 0
for i in range(1,11,1):
    if i % 2 == 0:
        result_1 = result_1 + i
print(result_1)

for i in range(1,101,1):
    if i % 3 ==0:
        print(i)

# 구구단 프로그램: 입력받은 수의 9까지의 배수를 출력해주는
num = int(input('몇 단을 볼까요?'))

for i in range(1,10,1):
    product = num * i
    print(num,'*',i,'=',product,'입니다.')

for i in range(1,11):
    for j in range(1,10):
        print(i,"*",j,"=",i*j)

# 다음은 천재 마트의 일자별 매출일에 대한 리스트입니다.
# sales = [2000, 3000, 4000, 1000, 1500, 3800, 200, 2900, 1300]
# for문을 돌며, 최고 매출이 일어난 일자와 최저 매출이 일어난 일자를 각각 파악하세요.
# 예시
# 최고 매출 : 3일차, 4000만원
# 최저 매출 : 7일차, 200만원
# 힌트 : answer와 같이 최고 매출 / 최저 매출을 기록할 수 있는 max_sales, min_sales를 정의하여 사용하세요.

high_sales = 3900
low_sales = 250
sales = [2000, 3000, 4000, 1000, 1500, 3800, 200, 2900, 1300]
for i in range(len(sales)):
    if high_sales < sales[i]:
        high_sales = sales[i]
        print(i+1,'일차,',high_sales)

for i in range(len(sales)):
    if low_sales > sales[i]:
        low_sales = sales[i]
        print(i+1,'일차,',low_sales)

# 사용자로부터 입력받은 숫자 n에 따라 높이가 n인 별 삼각형을 출력하는 프로그램을 작성하세요.

height = int(input('숫자를 입력해주세요.'))
for i in range(1,height+1):
    print("*"*i)