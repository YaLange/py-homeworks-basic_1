class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if lecturer.course == course and course in self.courses_in_progress:
            lecturer.grades.append(grade)

    def get_average_grade(self):
        total_grades = sum(sum(course_grades, []) for course_grades in self.grades.values())
        total_courses = sum(len(course_grades) for course_grades in self.grades.values())
        return total_grades / total_courses if total_courses > 0 else 0

    def __str__(self):
        average_grade = self.get_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f"Студент:\nИмя: {self.name}\nФамилия: {self.surname}\nПол: {self.gender}\n" \
               f"Средняя оценка за курсы: {average_grade}\n" \
               f"Курсы в процессе изучения: {courses_in_progress}\n" \
               f"Завершенные курсы: {finished_courses}\n"

    def __gt__(self, other):
        return self.get_average_grade() > other.get_average_grade()

    def __ge__(self, other):
        return self.get_average_grade() >= other.get_average_grade()

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        return self.get_average_grade() <= other.get_average_grade()

    def __eq__(self, other):
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        return self.get_average_grade() != other.get_average_grade()


class Lecturer:
    def __init__(self, name, surname, course):
        self.name = name
        self.surname = surname
        self.course = course
        self.grades = []

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades) if len(self.grades) > 0 else 0

    def __str__(self):
        average_grade = self.get_average_grade()
        return f"Лектор:\nИмя: {self.name}\nФамилия: {self.surname}\nКурс: {self.course}\n" \
               f"Средняя оценка за курс: {average_grade}\n"

    def __gt__(self, other):
        return self.get_average_grade() > other.get_average_grade()

    def __ge__(self, other):
        return self.get_average_grade() >= other.get_average_grade()

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        return self.get_average_grade() <= other.get_average_grade()

    def __eq__(self, other):
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        return self.get_average_grade() != other.get_average_grade()


student1 = Student("Иван", "Иванов", "М")
student2 = Student("Анна", "Петрова", "Ж")

lecturer1 = Lecturer("Петр", "Сидоров", "Python")
lecturer2 = Lecturer("Мария", "Кузнецова", "JavaScript")

student1.rate_lecturer(lecturer1, "Python", 8)
student1.rate_lecturer(lecturer1, "Python", 9)
student1.rate_lecturer(lecturer2, "JavaScript", 7)
student2.rate_lecturer(lecturer2, "JavaScript", 10)

print(student1)
print(lecturer1)
print(student2)
print(lecturer2)

print(f"Средняя оценка студента 1: {student1.get_average_grade()}")
print(f"Средняя оценка студента 2: {student2.get_average_grade()}")
print(f"Средняя оценка лектора 1: {lecturer1.get_average_grade()}")
print(f"Средняя оценка лектора 2: {lecturer2.get_average_grade()}")

if student1 > student2:
    print("Средняя оценка студента 1 выше, чем у студента 2")
elif student1 < student2:
    print("Средняя оценка студента 1 ниже, чем у студента 2")
else:
    print("Средняя оценка студента 1 равна средней оценке студента 2")

if lecturer1 > lecturer2:
    print("Средняя оценка лектора 1 выше, чем у лектора 2")
elif lecturer1 < lecturer2:
    print("Средняя оценка лектора 1 ниже, чем у лектора 2")
else:
    print("Средняя оценка лектора 1 равна средней оценке лектора 2")