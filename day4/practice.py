# 각각 등급 별로, 몇개의 보석이 있는지 알아 봅시다!
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grades = {} # 빈 딕셔너리

for i in gems:
    if i not in grades:
        grades[i] = 1 # 처음 키를 생성하고 값을 추가하는 과정
    else:
        grades[i] += 1
print(grades)

# 인기투표!
# 후보가 없는 인기투표

votes = ['세연','지민','수진','유진','화영',
         '수진','수진','수진','화영','화영','화영','지민','지민','지민','지민','지민','유진','유진']
print(len(votes))
result = {}

name = input('어떤 사람의 득표수가 궁금하세요? ')
print(votes.count(name))
for vote in votes:
    if vote in result:
        result[vote] += 1
    else:
        result[vote] = 1
print(result)

#quiz_1
# 다음의 리스트에서 소숫점을 제외한 평균값을 구하시오. ex) 3.1724일 경우 3을 출력
answer = 0
nums = [1, 7, 2, 3, 6, 1, 2, 5, 3, 4, 8, 7]
for i in range(len(nums)):
    answer = answer + nums[i]
print(round(answer/len(nums)))

#quiz_2
# 입력된 문자열을 뒤집은 문자열을 구하시오.
# ex) banana 입력 시 ananab 출력
word = input()

reversed_word = word[::-1]
print(reversed_word)

#quiz_3
# 주어진 배열 안의 값을 전부 2배로 만드시오.
# ex) [7, 2, 3]의 경우 [14, 4, 6]이 되어야 합니다.
nums = [7, 2, 9, 8, 4, 3, 5]

for i in range(len(nums)):
    nums[i] = nums[i] * 2
print(nums)

#quiz_4
# <별 찍기>
# 자연수 N을 입력받아, N줄까지 별을 출력하는 함수를 만드시오.
# 첫 번째 줄은 별이 1개이며, N번째 줄은 N개의 별이 찍혀야 합니다.

N = int(input('N을 입력해주세요.: '))

def print_stars(N):
   for i in range(1,N+1):
       print('*'*i)

print_stars(N)

#quiz_5
# <절댓값 구하기>
# A와 B 정수를 입력받아 두 수의 차의 절댓값을 반환하는 함수를 만드시오.
# 만약 7과 -3을 받았다면 10을 출력해야 한다.

A = int(input())
B = int(input())

def get_absolute_value(x, y):
    if A >= B:
        return A-B
    else:
        return -1*(A-B)

print(get_absolute_value(A, B))

#quiz_6
# <미출석 인원 찾기>
# 전체 출석부와 현재 출석한 인원이 리스트로 주어질 때, 출석하지 않은 인원을 출력하시오. (순서 굳이 상관 없음)
students = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # 전체 명단
attened = ['c', 'e', 'f', 'h']  # 출석 명단
non_attened = []

for student in students:
    if student not in attened:
        non_attened.append(student)
print(non_attened)

#quiz_7
# 다음과 같은 api 데이터가 있을 때, 모든 유저들의 이름을 모아보시오.
users = {
    'total_user': 3,
    'information': [
        {'name': 'alex', 'age': 3, 'license': True},
        {'name': 'june', 'age': 7, 'license': False},
        {'name': 'peter', 'age': 4, 'license': False}
    ]
}

names = []
for name in users['information']:
    names.append(name['name'])
print(names)  # ['alex', 'june', 'peter']

#quiz_8
# <수 정렬하기>
# 주어진 2차원 리스트를 기준에 따라서 정렬하시오.
# [앞쪽, 뒤쪽] 이라고 할 때, 뒤쪽이 '작은' 순서로 정렬하되 만약 같다면 앞쪽이 '큰' 순서대로 정렬하시오.
nums = [[70, 30], [70, 10], [20, 30], [50, 90], [40, 80], [80, 90], [10, 60]]
new_nums = []
for num in nums:
    if num[0] > num[1]:
        new_nums.append(num)
    if num[0] < num[1]:
        new_nums.append(num[::-1])
print(new_nums)

for num in nums:
    if num[0] > num[1]:
        continue
    elif num[0] < num[1]:
        num = num.sort(key=lambda x:-x)
print(nums)

nums.sort(key=lambda x:(x[1],-x[0]))
    

# 3,6,9 프로그램
for i in range(1,101):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        i = '짝!'
    
    print(i, end = '')

for i in range(1,11):
    print(i*10)

print('홈트레이닝 2주 계획입니다.')
for i in range(1,15):
    if i % 5 == 0:
        print(f'{i}일: 휴식일입니다.')
    else:
        print(f'{i}일: 스쿼트 - 윗몸 일으키기 - 유산소 운동')


for i in range(5):
    name = input()
    count = int(input())
    print(name*count)


