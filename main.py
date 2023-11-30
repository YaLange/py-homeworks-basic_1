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
        total_grades = sum(sum(lecturer.grades, []) for lecturer in self.lecturers.values())
        total_courses = sum(len(lecturer.grades) for lecturer in self.lecturers.values())
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
    def __init__(self, name, surname, course):
        super().__init__(name, surname)
        self.course = course
        self.grades = []

    def get_average_grade(self):
        total_grades = sum(self.grades)
        total_courses = len(self.grades)
        return total_grades / total_courses if total_courses > 0 else 0

    def __str__(self):
        average_grade = self.get_average_grade()
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {average_grade}"


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}"


# Пример использования и сравнения:
 lecturer1 = Lecturer("John", "Doe", "Python")
 lecturer2 = Lecturer("Jane", "Smith", "JavaScript")
 student1 = Student("Alice", "Brown", "Female")
 student2 = Student("Bob", "Johnson", "Male")
 reviewer1 = Reviewer("John", "Smith")
 reviewer2 = Reviewer("Jane", "Doe")

 reviewer1.courses_attached.append("Python")
 reviewer2.courses_attached.append("JavaScript")
 student1.courses_in_progress.append("Python")
 student2.courses_in_progress.append("JavaScript")
 lecturer1.grades = [9.5, 8.8, 9.2]
 lecturer2.grades = [9.7, 9.9, 8.5]

 print(reviewer1)
 print(reviewer2)
 print(lecturer1)
 print(lecturer2)
 print(student1)
 print(student2)

 # Сравнение лекторов
 if lecturer1 > lecturer2:
     print(f"{lecturer1.surname} лучше, чем {lecturer2.surname}")
 elif lecturer1 < lecturer2:
     print(f"{lecturer2.surname} лучше, чем {lecturer1.surname}")
 else:
     print("Оценки лекторов равны")

 # Сравнение студентов
 if student1 > student2:
     print(f"{student1.surname} лучше, чем {student2.surname}")
 elif student1 < student2:
     print(f"{student2.surname} лучше, чем {student1.surname}")
 else:
     print("Оценки студентов равны")