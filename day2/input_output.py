name = input('이름을 입력해 주세요.: ') #input 함수는 늘 문자열로 반환된다는 것을 잊지 말 것!

print(type(name))
print(name+"님은 출석이 되셨습니다.")

word1 = "hello"
word2 = "world"
print(word1, word2)

name = input('나의 이름은: ')
age = input('나의 나이는: ')
print('나는 '+name+' 입니다', end=":)")
age = int(age)
next_age = age+1
print(next_age)
print('내년의 나이는 '+str(next_age)+'살 입니다') # +는 문자열끼리 연결(공백 없이), ,는 정수형도 연결해줌(공백 생김)!

# print("내년에는 ", age+1, "살이 됩니다.")
# print(f"내년에는 {age+1}살이 됩니다.") # 나중에 배우게 될 f-string
# age = input('나의 나이는: ')
# print(age)
# int(age)
# print(int(age)+1)
# print("내년 나의 나이는 "+str(int(age)+1)+"살 입니다", end="!!")