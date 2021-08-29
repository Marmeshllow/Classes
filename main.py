class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and \
                course in lecturer.courses_attached and 0 < grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнии задания: {avg(self.grades)}\n' \
              f'Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student')
            return
        return avg(self.grades) < avg(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg(self.grades)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer')
            return
        return avg(self.grades) < avg(other.grades)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and \
                course in student.courses_in_progress and 0 < grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname} '
        return res


def avg(grade_dict, course='overall'):
    total = 0
    count = 0
    if course == 'overall':
        for elm in grade_dict.values():
            total += sum(elm)
            count += len(elm)
    else:
        for name, elm in grade_dict.items():
            if name == course:
                total += sum(elm)
                count += len(elm)
    if total > 0:
        res = round(total / count, 2)
    else:
        res = "Нет оценок"
    return res


def avg_people(course, *people):
    total = 0
    for person in people:
        total += avg(person.grades, course=course)
    res = round(total / len(people), 2)
    return res


lec = Lecturer('Yan', 'Pussivivch')
lec.courses_attached = 'Python'

lec2 = Lecturer('Pitter', 'Puker')
lec2.courses_attached = 'Python'

stu = Student('Vasya', 'Pupkin', 'male')
stu.courses_in_progress += ['Python']
stu.courses_in_progress += ['HTML']
stu.rate_hw(lec, 'Python', 10)
stu.rate_hw(lec, 'Python', 5)
stu.rate_hw(lec, 'Python', 7)
stu.rate_hw(lec2, 'Python', 9)
stu.finished_courses = 'Git'

stu2 = Student('Vika', 'Losina', 'female')
stu2.courses_in_progress = ['Python']
stu2.courses_in_progress += ['HTML']
stu2.rate_hw(lec, 'Python', 3)
stu2.rate_hw(lec, 'Python', 6)
stu2.rate_hw(lec, 'Python', 2)
stu2.rate_hw(lec2, 'Python', 4)
stu2.finished_courses = 'Git'

rev = Reviewer('Lass', 'Pesco')
rev.courses_attached += ['Python']
rev.courses_attached += ['HTML']

rev2 = Reviewer('Mill', 'Fallevich')
rev2.courses_attached += ['Python']
rev2.courses_attached += ['HTML']

rev.rate_hw(stu, 'Python', 7)
rev.rate_hw(stu, 'HTML', 5)
rev.rate_hw(stu2, 'Python', 8)
rev2.rate_hw(stu, 'Python', 7)
rev2.rate_hw(stu2, 'HTML', 5)
rev2.rate_hw(stu2, 'Python', 8)

lectures = [lec, lec2]
print(stu)
print(lec)
print(stu > stu2)
print(lec > lec2)
print(avg_people('Python', stu, stu2))
print(avg_people('Python', *lectures))
