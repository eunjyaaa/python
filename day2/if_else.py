# 조건문
# if 조건:
    # 코드블럭1
# else:
    # 코드블럭2

sale_rate = float(input('현재 할인율'))
price = 10000
condition = sale_rate >= 0.3

if condition:
    print('구매')
    print(price*(1-sale_rate))
else:
    print('구매하지 않습니다.')


#나이 판별기
age = int(input('당신의 나이는:'))
if age >= 20:
    print(age,'살','어른')
elif age >= 10:
    print(age,'살','청소년')
elif age >= 5:
    print(age,'살','어린이')
else:
    print(age,'살','영유아')