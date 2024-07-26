# while: 조건이 만족하는 동안 반복
# while 조건:
    # 조건에 따라 반복하고자 하는 코드
    # (중요!) while문 안에서 조건을 변화해 나갈 수 있어야 함

greetings = ['안녕', '니하오', '봉주르', '올라']
i = 0

while i < len(greetings):
    print(greetings[i]) 
    i += 1

print('반복이 중단되었습니다.')
print(i)

i = 1
while i <= 10:
    print(i)
    i += 1

i = 1
answer = 0

while i <= 10:
    answer = answer + i
    i += 1
print(answer)

i = 0
answer_1 = 0
while i <= 10:
    answer_1 = answer_1 + i
    i += 2
print(answer_1)

# break 만나기
names = ['티모시', '변우석', '이은선', '김지민', '김태현']
i = 0

while True:
    print(names[i])
    if names[i] == '이은선':
        print('우리반 슈퍼스타 영접!')
        break
    i += 1 # 'if문까지 검토를 하고, i번호를 늘리겠다.'는 의미! 만일 if문 전에 있다면, 첫번째 리스트에 원하는 원소가 있을 때 찾지 못함
print(i)

for i in range(len(names)):
    print(names[i])
    if names[i] == '이은선':
        print("잡았다 요놈!")
        break
print(i)

# continue 만나기
names = ['우석', '호재', '해주', '은지', '지은']
students = ['은지', '지은', '해주']

for name in names:
    if name in students:
        continue
    print(name,"너 누구얏")


