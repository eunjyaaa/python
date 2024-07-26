# 문자열 나누기
email = "elly9656@gmail.com"
email_lst = email.split('@') # @를 기준으로 나눠줌
print(email_lst)
print(type(email_lst))
print(email_lst[0])

print(id(email))
print(id(email_lst))

new_email = email.replace('gmail','naver') # 앞의 것을 뒤의 것으로 바꿔
print(new_email)

print("========================================")
temperature = input('온도를 입력해주셈')
print(temperature)
temp_list = temperature.split(',')
print(temp_list)

print("========================================")
# 이어붙여서 문자열 만들기
print("!".join('오늘은 금요일><')) # 사이사이에 느낌표 붙어짐

python_chr = list('python')
print(python_chr)

print("!".join(python_chr))
# print('<3'.join([1,2,3,4)]) 이 경우 리스트를 구성하는 원소들이 정수이기 때문에 에러가 발생한다

print("========================================")
# 탐색
print(email.find('!')) # 찾았는데, 없으면 -1 반환 (세련된 방식) # 리스트는 변동이 발생할 수 있어서 find 사용 불가
print(email.index('!')) # 찾았는데, 없으면? 에러 발생