# day1_wrapup_test

a = '456'
b = 789
print(int(a)+b)

c = " "
a = int(a)
b = 789
d = a // b
print(d) # 0
print(c != d)
print(not c==d)
print(not d)
print(c==d or c!=d)
print(bool(c) or bool(d))

# 대소 비교의 경우, 자료형 일치해야 함
# ==, !=의 경우 단순 비교로서 값이 일치하는지 여부만 판단함

# 백화점 VIP 판별 프로그램
money = int(input('소비금액 (단위:만원)'))
count = int(input('구매 횟수'))

if money >= 1000 and count >= 10:
    print("VIP")
elif money >= 1000 or count >= 10:
    print("우수고객")
else:
    print("일반고객")

is_male = input('남성인가요?')
if is_male == 'True':
    is_male = True # 변수 재할당
    print(is_male)
elif is_male == 'False':
    is_male = False
    print(is_male)
else:
    print('잘못입력하셨습니다.')