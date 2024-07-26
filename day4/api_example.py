# 구조화(api)
user1 = {'name':'alex', 'age': 37, 'license': True}
user2 = {'name':'kyle', 'age': 21, 'license': True}
user3 = {'name':'peter', 'age': 4, 'license': False}

user = {
    'total user': 3,
    'information':[
        {'name':'alex', 'age': 37, 'license': True},
        {'name':'kyle', 'age': 21, 'license': False},
        {'name':'peter', 'age': 4, 'license': False}
    ]
}

# Q1. 라이센스가 있는 인원들의 숫자 구하기
license_ppl = 0
for info in user['information']:
    if info['license'] == True:
        license_ppl += 1
print(license_ppl)

# Q2. 모든 사람의 나이의 평균 구하기
age_sum = 0
for ages in user['information']:
    age_sum += ages['age']
print(round(age_sum/user['total user']))

# Q3. 라이센스가 없는 사람들의 이름 모으기
no_license = []
for ppl in user['information']:
    if ppl['license'] == False:
        no_license.append(ppl['name'])
print('No license: ', no_license)


# print(len(user))
# print(type(user['information'])) # 리스트 형태로 조회됨

# info = user['information'] # 리스트로 바뀌기 때문에 인덱스 번호로 하나하나 조회 가능
# print(info[0]);print(info[1]);print(type(info[2])) # 각각은 dict

# for i in user['information']:
#     print(i['name'])

# user_sum_age = 0
# for i in user['information']:
#     user_sum_age += i['age']
# print(user_sum_age)
# print(user_sum_age/user['total user'])