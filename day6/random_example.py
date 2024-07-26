import random

# 랜덤한 int 값을 반환
ramdom_number = random.randint(1,45) #끝 숫자도 포함
print(ramdom_number) #40 #실행할 때마다 달라짐

# 랜덤한 사람을 뽑기?
students = ['은지','지은','은수',
            '수지','지나','나경','경수']

idx = random.randint(0, len(students)-1) # 무작위로 인덱스 번호를 추첨
print(f'{students[idx]}, 너 나와!')

studnet = random.choice(students) # 무작위로 리스트 안의 원소를 추첨
print(f'{studnet}~ 하이루')

# 리스트 원소중에서, n개를 무작위 선택 -> sample 활용
lucky_ppl = random.sample(students, 2) #리스트 안에서, 몇 개를 랜덤하게 뽑아낼 것인지!
print(lucky_ppl)
