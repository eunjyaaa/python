numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

for i in range(100):
    if i % 5 ==1:
        print('쿵', end=' ')
    elif i % 5==2:
        print('짝', end=' ')
    else:
        print(i, end = ' ')

# 45분 일찍 울리는 알람 프로그램
h = int(input('시 '))
m = int(input('분 '))

if (h >= 0 and h <= 23) and (m >= 0 and m <= 59):
    if m - 45 >= 0:
        print(h, m)
    elif m - 45 < 0 and h > 0:
        m = 59 - (44-m)
        h = h - 1
        print(h, m)
    elif  m - 45 < 0 and h == 0:
        m = 59 - (44-m)
        h = 23
        print(h, m)
else:
    print("다시 입력해주세요.")


#  주사위 굴리기 프로그램
a = int(input('첫 번째 주사위'))
b = int(input('두 번째 주사위'))
c = int(input('첫 번째 주사위'))

if (a >= 1 and a <= 6) and (b >= 1 and b <= 6) and (c >= 1 and c <= 6):
    if a == b and a == c and b == c:
        print(10000+a*1000)
    elif a != b and a != c and b != c:
        if a > b and a > c:
            print(a*100)
        elif b > a and b > c:
            print(b*100)
        elif c > a and c > b:
            print(c*100)
    elif a == b and b != c or a == c and b != c:
        print(10000+a*100)
    elif b == c and a != c:
        print(10000+b*100)
else: 
    print("다시 입력하세요.")

# 영수증 계산 프로그램
shop_lists = [250000, 20000, 5, 30000, 2, 10000, 6, 5000, 8]
result = 0
i = 1
while i < len(shop_lists):
    result = result + shop_lists[i]*shop_lists[i+1]
    i += 2
print(result)
if shop_lists[0] == result:
    print(result, ' 로 일치합니다.')
else:
    print("틀렸습니다.")

# 고객 유형 별 할인율 계산 프로그램
# for 반복문 활용
purchases = 0
count = 0
new_purchase = 100
A = [100, 25, 50, 140, 33, 40, 420, 1, 4, 12]
# A.append(100) # 가방 추가 구매 이후 -> 고객 등급의 변화 여부 확인 가능

for i in range(len(A)):
    purchases = purchases + A[i]
    count = i + 1 # count += 1
print(purchases, '만원') #print(f'{purchases}만원 구매하셨습니다.')
print(count, '번')

# 할인된 가격 조회
if purchases >= 1000 and count >= 10:
    print('VIP')
    print(int(new_purchase * 0.85), '만원')
elif purchases >= 1000 or count >= 10:
    print('우수고객')
    print(int(new_purchase * 0.9), '만원')
else:
    print('일반고객')
    print(int(new_purchase * 0.95), '만원')

# while로 해보기
i = 0
purchases = 0
count = 0
new_purchase = 100
A = [100, 25, 50, 140, 33, 40, 420, 1, 4, 12]

while i < len(A): # range의 경우 대소비교가 되지 않음
    purchases = purchases + A[i]
    count = i +1
    i += 1
print(purchases, '만원')
print(count, '번')