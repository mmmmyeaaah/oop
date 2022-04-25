class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_course.append(course_name)   

    def rate_lecture(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress and 0 < grade < 11:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'   

    def __str__(self):
        str_courses_in_progress = ', '.join(i for i in self.courses_in_progress)
        str_finished_courses = ', '.join(i for i in self.finished_courses)
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {grades(self.grades)} \nКурсы в процессе изучения: {str_courses_in_progress}  \nЗавершенные курсы: {str_finished_courses}'   

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не является студентом')                     
            return
        else:
            if grades(self.grades) == grades(other.grades):
                print('Все молодцы!')
            elif grades(self.grades) > grades(other.grades):
                print(f'{self.name} умнее!')
            else:
                print(f'{other.name} умнее!')    
 
     
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
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {grades(self.grades)}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не является Лектором!')                     
            return
        else:
            if grades(self.grades) == grades(other.grades):
                print('Все молодцы!')
            elif grades(self.grades) > grades(other.grades):
                print(f'{self.name} лучше!')
            else:
                print(f'{other.name} лучше!')     


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and 0 < grade < 11:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'  


def grades(dict_):
    count = 0
    grade = 0
    for i in dict_.values():
        for k in i:
            grade += k
            count += 1
    if count == 0:
        return 0
    else:
        return grade / count       


def count_grade_student(list_student, course):
    grades = 0
    count = 0
    for student in list_student:
        if course in student.courses_in_progress and course in student.grades:
            for grade in student.grades[course]:
                grades += grade
                count += 1
        else:
            print(f'Ученик {student.name} курс {course} не изучал!')        
    if count != 0:
        print(f'Средняя оценка учеников за курс {course}: {int(grades / count)}')      
    else:
        return    


def count_grade_lecturer(list_lect, course):
    grades = 0
    count = 0
    for lecturer in list_lect:
        if course in lecturer.courses_attached and course in lecturer.grades:
            for grade in lecturer.grades[course]:
                grades += grade
                count += 1
        else:
            print(f'Лектор {lecturer.name} не ведёт курс {course}!')
    if count != 0:
        print(f'Средняя оценка лекторов за курс {course}: {int(grades / count)}')                                   
    else:
        return    
                            
   

well_lecturer = Lecturer('Pit', 'Byke')
well_lecturer.courses_attached += ['Git']

cool_lecturer = Lecturer('Dr.', 'Connors')
cool_lecturer.courses_attached += ['Git']

best_lecturer = Lecturer('Tony', 'Stark')
best_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['Git']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.rate_lecture(well_lecturer, 'Git', 2)
best_student.finished_courses += ['C#']
best_student.finished_courses += ['java']

looser_student = Student('Eddy', 'Broke', 'm')
looser_student.courses_in_progress += ['Python']
looser_student.courses_in_progress += ['Git']
looser_student.rate_lecture(cool_lecturer, 'Git', 10 )
looser_student.rate_lecture(best_lecturer, 'Git', 8)

stupid_student = Student('Vasia', 'Pypkin', 'm')
stupid_student.courses_in_progress += ['Git']
stupid_student.finished_courses +=['Physical Education']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(best_student, 'C++', 10)
cool_reviewer.rate_hw(looser_student, 'Python', 5)
cool_reviewer.rate_hw(looser_student, 'Git', 2)
cool_reviewer.rate_hw(stupid_student, 'Git', 1)

list_students = [best_student, stupid_student, looser_student]
list_lectors = [cool_lecturer, best_lecturer, well_lecturer]

count_grade_student(list_students, 'Git')
count_grade_student(list_students, 'Python')
count_grade_student(list_students, 'Pythone')

count_grade_lecturer(list_lectors, 'Git')
count_grade_lecturer(list_lectors, 'Python')

print(cool_reviewer)
print(well_lecturer)
print(best_lecturer)
print(cool_lecturer)
print(best_student)
print(looser_student)
print(stupid_student)
best_student.__lt__(looser_student)
cool_lecturer.__lt__(well_lecturer)
