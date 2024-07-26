# 리스트
numbers = [10, 20, 30, 40, 50] # list(range(10,51,10))
print(type(numbers))

# 리스트 = 순서가 있는 자료형
print(numbers[2]) # 인덱싱 = 순서, 위치로 값을 조회

# 리스트 = 가변 자료형 (mutable)
numbers[2] = '30입니다.'
print(numbers)
print(numbers[2:4:1])
print(numbers[-3:-1:1]) # 맨 끝이 -1 이다!

numbers.append(60) # 리스트의 마지막 위치에 새 원소를 삽입
print(numbers)

last_value = numbers.pop() # 마지막 원소를 삭제
print(last_value)
print(numbers)

# (주의) 문자열 == 불변 자료형 (immutable)

s = 'python'
s = 'P'+s[1:] 
p = list(s)
print(p)

new_s = s.capitalize()
print(new_s)
q = list(new_s) # 문자열은 불변이나, 형변환된 리스트는 가변이기에 리스트 상태에서는 수정이 가능하다!!
print(q)