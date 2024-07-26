subjects = ["Python", "Java", "Python", "C++", "Python", "Java", "C++", "Python", "Data Science", "Data Science", "Python"]

# max_subject = 0

# for subject in subjects:
#     if subjects.count(subject) > max_subject:
#         max_subject = subjects.count(subject)
# print(subject)

max_subject = {}

for subject in subjects:
    if subject not in max_subject:
        max_subject[subject] =1
    else:
        max_subject[subject] += 1
print(max_subject)

most_subject = ''
most_count = 0
for subject in max_subject:
    if max_subject[subject] > most_count:
        most_subject = subject
        most_count = max_subject[subject]
print(most_subject)


scores = [55, 60, 65, 70, 75, 80, 85, 90, 95]
scores.sort()
print(scores)
print(' <사분위수> ')
Q1 = sum(scores[:4])/4
Q3 = sum(scores[5:])/4
print(Q3-Q1)

print(' <범위> ')
print(max(scores)-min(scores))