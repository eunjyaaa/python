shop_lists = [250000, 20000, 5, 30000, 2, 10000, 6, 5000, 8]

amount = sum(shop_lists)
count = len(shop_lists)

def grade_classifer(amount, count):
    condition1 = amount >= 1000
    condition2 = count >= 10

    if condition1 and condition2:
        return('vip')
    elif condition1 or condition2:
        return('우수 고객')
    else:
        return('일반 고객')
    
grade = grade_classifer(amount, count)
print(grade)

print('====================================')
price = int(input('새로 구매할 제품의 할인 전 가격:'))

if grade == 'VIP':
    price *= 0.85
elif grade == '우수 고객':
    price *= 0.9
else:
    price *= 0.95

print(f'새로 구매할 가방은 {int(price)}만원입니다.')

shop_lists.append(price)
new_grade = grade_classifer(sum(shop_lists),len(shop_lists))

print(f'구매 후 등급은 "{new_grade}" 입니다.')

# 별 찍기 문제
# 매개변수 O, 반환값 X
N = int(input('N을 입력해주세요. '))
def star_maker(N):
    for i in range(1,N+1):
        print('*'*i)
print('함수 호출을 시작합니다.')
star_maker(N) # 함수 내용(별들을 출력하라!)에 따라서 삼각형이 출력된 것, 결과값이 함수에 반환되지 않았음.
print(f'{N}이/가 입력되었습니다.')

# 잘못된 케이스
# 경우 1 : 입력받아야 하는데, 입력을 받지 못함
# print_stars()

# 경우 2 : 반환값이 없는데, 반환받으려 하는 경우
# p = print_stars(N)
# print(p) # 반환되는 값이 없음에도 불구하고 받으려고 했기 때문에 
#         # 파이썬에서 자체적으로 "없다" 라는 None을 할당해 버림

# print_stars(N) 정의한 함수를 올바르게 호출한 코드

# print() : print 함수안에 들어간 리스트, 문자열, 숫자건 "출력" / 함수의 결과값으로 반환받는 것이 없음
# return : 함수의 결과를 반환

#####################################################################

# return을 이용한 별찍기 문제
# N = int(input('N을 입력해주세요. '))
# def new_stars(N):
#     result = ''
#     for i in range(1, N+1):
#        result = result + '*'*i + '\n' #\n은 이스케이프 코드로서 줄바꿈에 이용함
#     print('함수 끝')
#     return result

# p = new_stars(N)
# print(p) 


# <절댓값 구하기>
# A와 B 정수를 입력받아 두 수의 차의 절댓값을 반환하는 함수를 만드시오.
# 만약 7과 -3을 받았다면 10을 출력해야 한다.

A = int(input('A를 입력해주세요. '))
B = int(input('B를 입력해주세요. '))

def get_absolute_value(X, Y):
    if A >= B:
        return A-B
    else:
        return -1 * (A-B)

result = get_absolute_value(A,B)
print(result)