import datetime
a = [1, 2, 3]
b = ['q', 'w', 'e']

dict = dict(zip(a,b))
print(dict)
sp = [[1, 2, 3], [4, 5, 6]]
sp1 = sp[0]
sp2 = sp[1]
sp1.extend(sp2)
print(sp1)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i in a:
    for y in b:
        if i==y:
            print(i)

d={'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

l=[]
for i in d:
    l.append(d[i])
l.sort()
timenow = datetime.datetime.now()
timeday = "2019 12 1"
parsed_date = datetime.datetime.strptime(timeday, "%Y %m %d")
print(parsed_date.year)

yearage = timenow.year - parsed_date.year
print(yearage)

a = [1, 2, 3]
b = ['q', 'w', 'e']
d={}
for i in range(len(a)):
    d[a[i]] = b[i]
print(d)
sl={i:y for i in a for y in b}
print(sl)
spisok = [i+1 for i in range(10)]
print(spisok)
def quadro(a):
    return a**2

res=list(map(quadro,spisok))
print(res)
res2=list(map(lambda x:x**3,spisok))
print(res2)
res3=list(filter(lambda x:x % 2==0,spisok))
print(res3)

numb=[1,2,3,4,5]
def um(a):
    res=1
    for i in a:
        res*=i
    return res
print(um(numb))

"""
Создать класс Person с атрибутами fullname, age, is_married
2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке
3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks, который был бы словарем, где ключ это название урока, а значение - оценка.
4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам
5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.
6. Добавить в класс Teacher атрибут уровня класса salary
7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к стандартной зарплате прибавляется бонус 5% за каждый год опыта свыше 3х лет.
8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики добавляются в список и список возвращается функцией как результат.
10. Вызвать функцию create_students и через цикл распечатать всю информацию о каждом ученике с его оценками по каждому предмету. Также рассчитать его среднюю оценку по всем предметам.

"""
class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        return f"Имя: {self.fullname}, " \
               f"Возраст: {self.age}, " \
               f"Статус: {self.is_married}"

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def  introduce_myself(self):
        return super().introduce_myself()

    def calculate_average_mark(self):
        sumofmarks = sum(self.marks.values())
        return sumofmarks/len(self.marks)

class Teacher(Person):
    def __init__(self, fullname, age, is_married, exp_year):
        super().__init__(fullname, age, is_married)
        self.exp_year = exp_year

    def  introduce_myself(self):
        return super().introduce_myself()

    def selarycount(self):
        standart = 6000
        if self.exp_year>=3:
            selaryall = standart + (self.exp_year-3)*(5 * standart / 100)
        else:
            selaryall = standart
        return selaryall

    def get_fullname(self):
        return self.fullname
    old = property(get_fullname)

t1=Teacher("Иван", 20, "Не женат",4)
print(t1.introduce_myself())
print(t1.selarycount())
print(t1.old+"<--")

print("-"*50)

def create_students():
    markslist1 = {"математика": 5, "физика": 5}
    studentobj1 = Student("Иван1", 20, "Не женат",markslist1)

    markslist2 = {"математика": 4, "физика": 4}
    studentobj2 = Student("Иван2", 20, "Не женат", markslist2)

    markslist3 = {"математика": 3, "физика": 3}
    studentobj3 = Student("Иван3", 20, "женат", markslist3)

    listofstudents = [studentobj1,studentobj2,studentobj3]



    return listofstudents

student_list = create_students()

# Вывод информации о каждом ученике и его оценках
for student in student_list:
    print(student.introduce_myself())
    for subject, mark in student.marks.items():
        print(f"Оценка по предмету {subject}: {mark}")
    average_mark = student.calculate_average_mark()
    print(f"Средняя оценка: {average_mark}\n")






