# 객체지향프로그래밍

class Student(): # 학생 설계
    population = 0
    status = '피곤함 :('

    def __init__(self, name): # 괄호 뒤는 매개변수
        self.name = name
        self.status = Student.status
        self.stat = 0
        Student.population += 1

    def study(self):
        self.stat += 1
        print(f'나, {self.name}')
        print('파이썬 뽀개고, 데이터 분석 처리하러 가는 중...')

    def eat(self, menu):
        if menu == '떠뽀끼':
            self.status = '배불띠 ><'
        elif menu == '피자':
            self.status = '쏘쏘'
        else:
            self.status = '윽'
        return f"행복한 {self.name}가 되었어욤"
    
student1 = Student('은지')
print(student1.name)
print(Student.population)
print(student1.status)
student1.study()
student1.study()

print(student1.stat)
print(student1.status)    

print(student1.status)

student1.eat('떠뽀끼')
print(student1.status)

print("===================================================================")
student2 = Student('루피')
print(Student.population) # Student라는 클래스 전체의 population 구하기
print(student2.name)
print(student2.status)
student2.study()
student2.study()
student2.study()
student2.study() # 루피 스탯 업그레이드
print(student2.stat)
student2.eat('피자')
print(student2.status)