student = {'name':'alex', 'age':16}

# 조회
print(student['age'])
# 만약 없는 키를 조회하고자 한다면?]
print(student['license']) # error 발생

# 조회를 좀 더 세련되게..
# 없으면, 
print(student.get('license','없다 요놈아'))

print("==========================================")
student['license'] = True # 딕셔너리는 가변적이므로 자료의 추가가 자유로움
print(student) # 추가한 이후 다시 딕셔너리 출력

student.update({'name':'elly'}) # 하나씩만 업데이트됨
print(student)

student.pop('age') # k&v 모두 사라짐!!!!!
print(student)

print(student.pop('nationality',-1)) # 없으면 쉼표 뒤의 값 출력
print(student)

print("==========================================")
print(student.keys()) # 특정 값을 가진 key는 어떻게 뽑징? key와 value를 뒤바꿔서... 구하기도
print(student.values())

print("==========================================")
for k in student:
    print(k) # key만 가져옴

for k,v in student.items():
    print(k,v) # key와 vaule 값 모두를 출력함!
