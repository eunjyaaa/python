# 구구단 만들기
import time
for i in range(1,10):
    print(f'{i}단 시작합니다!!!!')
    time.sleep(1)
    for j in range(1,10):
        print(f'{i}X{j}={i*j}')
    if j == 9:
        print(f'{i}단 끝났습니다.')
        time.sleep(1)

