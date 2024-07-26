# 리스트 메소드

numbers = [4,2,6,1,5,5,2,4,7,9,8]

print(len(numbers))
print(id(numbers))

print("=========================================")
numbers.append(10) # 아무 것도 반환하지 않음
print(numbers)
print(id(numbers)) # 주소는 바뀌지 않음

print("=========================================")
last = numbers.pop()
print(last)
print(id(numbers)) # 여전히 주소가 바뀌지 않음

print("=========================================")
numbers.sort()
print(numbers) # 기본값: 오름차순 정렬

numbers.sort(key=lambda x:-x) # 내림차순 정렬 # 외우세용
print(numbers)

# lamda란?
# 사용자 정의 함수 -> 익명함수
# lambda 매개변수:결과값

print("=========================================")
new_numbers = sorted(numbers)
print(numbers)
print(new_numbers) # 기존 리스트를 오름차순으로 정렬하여, 새로운 리스트를 출력

print(numbers[::-1]) # 뒤집어서 새로운 리스트를 반환한다.
print(numbers) # 뒤집어서 새로운 리스트를 반환하는 것, 기존 리스트에는 변함 없음

# 기존의 리스트 그 자체를 뒤집는 방법
numbers.reverse()
print(numbers)

print(list(reversed(numbers))) # 새로 뒤집힌 리스트를 반환
print(numbers)

# 추가
print("=========================================")
numbers.insert(1,100) # insert(위치, values)
print(numbers)

numbers.extend([10,100,20]) # 괄호 안의 리스트의 원소를 추가해줌. append 구문에서 리스트 자체가 추가되는 것과는 다름
print(numbers)

print("=========================================")
numbers.extend('python') # 문자열을 구성하는 원소 하나하나가 리스트에 추가됨. 즉 'p', 'y' ...으로 추가되는 식
numbers.append('python') # 문자열이 통으로 추가됨

print("=========================================")
votes = ['월리', '춘식이', '쿠로미', '루피','케로로','도라에몽'
         , '쿠로미', '쿠로미', '쿠로미', '쿠로미','루피','루피','루피','루피'
         , '춘식이', '춘식이', '춘식이','케로로','도라에몽','케로로','도라에몽']

cnt = 0
for vote in votes:
    if vote == '쿠로미':
        cnt += 1
print(cnt)

# 리스트에서 어떠한 값의 갯수를 세어주는 메소드

candidate = input('득표수를 알고 싶은 후보자를 입력해 주세요.')
print(votes.count(candidate))

# 처음 나타난 위치를 찾고 싶을 때, index
print(votes.index('루피'))
votes.remove()

# 다음은 천재 마트의 일자별 매출일에 대한 리스트입니다.
# for문을 돌며, 최고 매출이 일어난 일자와 최저 매출이 일어난 일자를 각각 파악하세요.
# 예시
# 최고 매출 : 3일차, 4000만원
# 최저 매출 : 7일차, 200만원
# 힌트 : answer와 같이 최고 매출 / 최저 매출을 기록할 수 있는 max_sales, min_sales를 정의하여 사용하세요.

sales = [2000, 3000, 4000, 1000, 1500, 3800, 200, 2900, 1300]
max_index = 0
max_sales = sales [0]

min_index = 0
min_sales = sales[0]

index = 0
for sale in sales:
    if max_sales < sale:
        max_sales = sale
        max_index = index

    if min_sales > sale:
        min_sales = sale
        min_index = index
    
    index += 1

print(f'최고 매출: {max_index+1}일차, {max_sales}만원')

# 리스트의 메소드, 내장함수를 이용해서
# 천재마트의 최고 매출과 최저매출, 각각의 매출이 발생한 일자

sales = [2000, 3000, 4000, 1000, 1500, 3800, 200, 2900, 1300]

print(f'{sales.index(max(sales))+1}일차: {max(sales)}만원')
print(f'{sales.index(min(sales))+1}일차: {min(sales)}만원')