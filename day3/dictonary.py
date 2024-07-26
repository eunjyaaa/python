numbers = ['alex', 20, True, 7000]

# 딕셔너리: 가변 자료형
numbers_dict = {'name':'alex', 'age':'20', 'license':True, 'salary':7000}
print(numbers_dict['salary'])

numbers_dict['salary'] += 1000
print(numbers_dict)

gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1] #gem을 돌아가며, 각 원소의 개수를 구함
grades = {1:0, 2:0, 3:0}

for i in gems:
    grades[i] += 1
print(grades)

# gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
# for i in gems:
#     print(i)
#     if i == 1:
#         break
#     i += 1
# print('잡았다 요놈!')

# 잘못된 코드
# salary = [1,2,4,5,6,200,500,260]

# i = 0
# while i < len(salary):
#     if salary(i) < salary(i+1):
#         salary.pop(i+1)
#     i += 1
#     if len(salary) == 1:
#         break
#     print('끝')

# 정답 코드
salary = [4, 1, 5, 6]

while True:
    for i in range(len(salary) - 1):
        if salary[i] > salary[i + 1]:
            salary.pop(i)
            break # 안쪽에 있는 루프를 끝내고 다시 맨 처음으로 돌아간다는 뜻!!
        elif salary[i] < salary[i + 1]:
            salary.pop(i + 1)
            break
    if len(salary) == 1:
        print(f'최소 임금값은 {salary[0]}입니다.') # 어차피 하나의 원소만 남게될 것이기 때문
        break

salary = [4, 1, 5, 6]
while True:
    for i in range(len(salary)-1):
        if salary[i] > salary[i+1]:
            salary.pop(i+1)
            break
        elif salary[i] < salary[i+1]:
            salary.pop(i)
            break
    if len(salary) == 1:
        print(f'최대 임금값은 {salary[0]}입니다.')
        break




    


