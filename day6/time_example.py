import time

print('time 모듈 어떻게 작동하는지 확인할게요.')
time.sleep(1)
print('확인했지?')

for i in range(5):
    print(5-i)
    time.sleep(1)
print('어떻게 작동하는지 확인하셨죠?')

print("==================로또 번호 출력 프로그램=================================")
# 1. 프로그램을 실행과 동시에 `5초의 카운트다운`이 진행된다. 1초가 흐를 때 마다 `“4초 남았습니다.”`와 같이 남은 시간을 출력한다.
# 2. 카운트다운이 종료되면, 1부터 45까지의 수 중 6개의 숫자를 무작위로 추출한다.
# 3. 6개의 숫자를 오름차순으로 정렬하여 출력한다.

import random

for i in range(5):
    print(f'{5-i}초 남았습니다.')
    time.sleep(1)
random_nums = random.sample(range(1,45),6) # 여러개를 무작위로 가져오고 싶을 때 sample 함수 이용!
lotto_num = random_nums[:-1]
lotto_bonus = random_nums[-1]

random_nums.sort()
print(f'로또 번호 {random_nums}')
print(f'보너스 번호 {lotto_bonus}')


