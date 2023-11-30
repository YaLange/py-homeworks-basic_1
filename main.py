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
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {average_grade}\n" \
               f"Курсы в процессе изучения: {courses_in_progress}\n" \
               f"Завершенные курсы: {finished_courses}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def get_average_grade(self):
        total_grades = sum(self.grades)
        total_ratings = len(self.grades)
        return total_grades / total_ratings if total_ratings > 0 else 0

    def __str__(self):
        average_grade = self.get_average_grade()
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {average_grade}"


def calculate_average_student_grade(students, course):
    total_grades = 0
    total_students = 0
    for student in students:
        if course in student.courses_in_progress:
            course_grades = student.grades.get(course, [])
            total_grades += sum(course_grades)
            total_students += len(course_grades)
    return total_grades / total_students if total_students > 0 else 0


def calculate_average_lecturer_grade(lecturers, course):
    total_grades = 0
    total_lecturers = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            total_grades += sum(lecturer.grades)
            total_lecturers += len(lecturer.grades)
    return total_grades / total_lecturers if total_lecturers > 0 else 0


# Создаем экземпляры классов
student1 = Student("Иван", "Иванов", "мужской")
student2 = Student("Анна", "Петрова", "женский")

lecturer1 = Lecturer("Дмитрий", "Смирнов")
lecturer2 = Lecturer("Елена", "Кузнецова")

# Вызываем методы
student1.courses_in_progress.append("Математика")
student1.finished_courses.append("Физика")
student2.courses_in_progress.append("Физика")

student1.rate_lecturer(lecturer1, "Математика", 5)
student2.rate_lecturer(lecturer1, "Физика", 4)
student1.rate_lecturer(lecturer2, "Математика", 3)

print(student1)
print()
print(student2)

print(lecturer1)
print()
print(lecturer2)

# Подсчет средней оценки по домашним заданиям для определенного курса
students = [student1, student2]
course = "Математика"
average_grade = calculate_average_student_grade(students, course)
print(f"\nСредняя оценка за домашние задания по курсу {course}: {average_grade}")

# Подсчет средней оценки за лекции для определенного курса
lecturers = [lecturer1, lecturer2]
course = "Математика"
average_grade = calculate_average_lecturer_grade(lecturers, course)
print(f"\nСредняя оценка за лекции по курсу {course}: {average_grade}")