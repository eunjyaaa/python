# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

word = input()
alpa = {}

for i in range(len(word)):
    word = word.upper()
    if word[i] not in alpa:
        alpa[word[i]] = 1
    else:
        alpa[word[i]] += 1
print(alpa)

# if len([k for k,v in alpa.items() if max(alpa.values)==v]) == 1:
#     print(alpa, key=alpa.get)
# else:
#     print('?') zzzzzzzzzzzzzzz..............


print("=========섭시/화씨 변환하기=========")

# 섭씨 → 화씨	[°F] = [°C] × 1.8 + 32
# 화씨 → 섭씨	[°C] = ([°F] − 32) / 1.8

# 1. 섭씨에서 화씨로 변환하는 함수 만들기
C = int(input())

def c_to_f(X):
    return round(1.8*X + 32)
F = c_to_f(C)
print(F)

# 2. 섭씨 리스트를 화씨 리스트로 변환하기
celsius_list = [30,27,28,31,30,31,33]
fahrenheit_list = []

for i in range(len(celsius_list)):
    fahrenheit_list.append(c_to_f(celsius_list[i]))

print(fahrenheit_list)

# 섭씨를 입력받아 리스트에 저장. q가 입력되면 입력을 멈추고, q가 입력되지 않으면 숫자를 리스트에 저장

celsius_list = []

while True:
    x = input('섭씨를 입력해주세요: (숫자 입력, 중단을 하고 싶으시면 q를 입력하세요).')

    if x == 'q':
        break
    else:
        celsius_list.append(int(x))

print(f'입력받은 섭씨 온도의 리스트: {celsius_list}')

new_celsius_list = []
for cel in celsius_list:
    cel = c_to_f(cel)
    new_celsius_list.append(cel)
print(new_celsius_list)







