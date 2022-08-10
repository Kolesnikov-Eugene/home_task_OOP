from statistics import mean
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grades = []
        self.avg_grade = None


    def lecturer_rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

            lecturer.avg_grades = [i for item in lecturer.grades.values() for i in item]
            lecturer.avg_grade = mean(lecturer.avg_grades)
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grade}\n'
                f'Курсы в процессе завершения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}')

    def __lt__(self, other):
        return self.avg_grade < other.avg_grade

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        #self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        self.avg_grades = []
        self.avg_grade = None


    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade}'

    def __lt__(self, other):
        return self.avg_grade < other.avg_grade



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]

            student.avg_grades = [i for item in student.grades.values() for i in item]
            student.avg_grade = mean(student.avg_grades)
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

ivan = Student('Ivan', 'Ivanov', 'male')
petr = Student('Petr', 'Petrov', 'male')
anna = Lecturer('Anna', 'Petrova')
elena = Lecturer('Elena', 'Gradova')
alex = Reviewer('Alexander', 'Ponomarev')
serg = Reviewer('Sergei', 'Grygoriev')

ivan.courses_in_progress += ['Python']
petr.courses_in_progress += ['Java']
anna.courses_attached += ['Python']
elena.courses_attached += ['Java']
alex.courses_attached += ['Python']
serg.courses_attached += ['Java']

ivan.lecturer_rate(anna, 'Python', 10)
ivan.lecturer_rate(anna, 'Python', 8)
petr.lecturer_rate(elena, 'Java', 7)
petr.lecturer_rate(elena, 'Java', 10)
alex.rate_hw(ivan, 'Python', 10)
alex.rate_hw(ivan, 'Python', 9)
serg.rate_hw(petr, 'Java', 7)
serg.rate_hw(petr, 'Java', 10)

print(petr)
print(anna)
print(petr < anna)

students_list = [ivan, petr]
lecturers_list = [anna, elena]
def avg_student_grade(students, course):
    avg = []
    for student in students_list:
        if course in student.courses_in_progress:
            avg.append(student.avg_grade)

    return mean(avg)

print(avg_student_grade(students_list, 'Python'))

def avg_lecturer_grade(lecturers, course):
    avg = []
    for lecturer in lecturers_list:
        if course in lecturer.courses_attached:
            avg.append(lecturer.avg_grade)

    return mean(avg)

print(avg_lecturer_grade(lecturers_list, 'Python'))










