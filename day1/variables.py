# =: 할당 연산자
    # 형태: 변수이름 = 변수의 값

name = "eunji"
age = 23
is_male = False

print("이름은: ")
print(name)

print("나이는: ")
print(age)

print("남자인가요?: ")
print(is_male)

# 변수 이름 짓기: 알파벳, 언더바, 숫자 조합으로 활용 / 띄어쓰기 안 됨
# del name: 변수를 삭제하는 예약어 / 변수 지정 불가! / 예약어가 덮어써지지 않도록 주의

number = 1
number = 2
number = 3

print(number) # 재할당된 변수의 경우 가장 마지막 값이 출력됨

x = 20
y = x
print(x); print(y)

x,y = 10, 20
print(x+y)

print(bool("0.0"))