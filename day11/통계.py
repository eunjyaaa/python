print("=========================== 최빈값 파이썬으로 구하기 =================================")

subjects = ["Python", "Java", "Python", "C++", "Python", "Java", "C++", "Python", "Data Science", "Data Science", "Python"]

max_subject = 0

for subject in subjects:
    if subjects.count(subject) > max_subject:
        max_subject = subjects.count(subject)
print(subject)

max_subject = {}

for subject in subjects:
    if subject not in max_subject:
        max_subject[subject] =1
    else:
        max_subject[subject] += 1
print(max_subject)

print(" < for 문으로 최빈값 구하기> ")
most_subject = ''
most_count = 0
for subject in max_subject:
    if max_subject[subject] > most_count:
        most_subject = subject
        most_count = max_subject[subject]
print(most_subject)

for sbt, cnt in max_subject.items():
    if cnt > most_count:
        most_count = cnt
        most_subject = sbt
print(f"가장 많이 나타난 과목, 최빈 과목은 {most_subject}, 나타난 횟수는 {most_count} 입니다.")

print(" <내장함수로 최빈값 구하기> ")
from collections import Counter
result = Counter(subjects)
print(result) # 한 번에 과목별 결과를 집계해줌
print(result.most_common(1))

print("===========================범위와 사분위수 구하기=================================")
scores = [55, 60, 65, 70, 75, 80, 85, 90, 95]
scores.sort()
print(scores)

print(' <범위> ')
print(max(scores)-min(scores))

print(' <사분위수> ')
print(scores[-3]-scores[2])
# 두 개 모두 데이터의 변동성을 반영하며, IQR의 경우 이상치의 영향을 단순 범위에 비해 덜 받음.

print("=========================== 분산과 표준편차의 이해 =================================")
A = [70, 75, 80, 85, 90]
B = [70, 80, 80, 80, 90]

import numpy as np

A_var = np.var(A)
B_var = np.var(B)

print(A_var)
print(B_var)

print(np.std(A)) # 표준편차 구하는 내장함수
print(np.std(B))

print("=========================== 가설 검증 =================================")
