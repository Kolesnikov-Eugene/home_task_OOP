from statistics import mean
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_gardes = [i for item in self.grades.values() for i in item]

    def lecturare_rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and (course
        in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        #avg = [i for item in self.grades.values() for i in item]
        avg = mean(self.avg_gardes)
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_garde}'
                f'Курсы в процессе завершения: {self.courses_in_progress}'
                f'Завершенные курсы: {self.finished_courses}')

    def __lt__(self, other):
        return self.avg_garde < other.avg_grade



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avg_gardes = [i for item in self.grades.values() for i in item]

    def __str__(self):
        #avg = [i for item in self.grades.values() for i in item]
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_garde}'

    def __lt__(self, other):
        return self.avg_garde < other.avg_grade



class Reviwer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

# gr = {'c1': [1, 2, 3], 'c2': [4,5]}
# avg = [i for item in gr.values() for i in item]
# for item in gr.values():
#     for i in item:
#         avg.append(i)

print(avg)

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)
