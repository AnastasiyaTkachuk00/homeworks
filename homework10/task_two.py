class Student:
    def __init__(self, name, surname, group_number, great):
        self.name = name
        self.surname = surname
        self.group_number = group_number
        self.great = great

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValidationError('Name must be string')

        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise ValidationError('Surname must be string')

        self._surname = value


class ValidationError(Exception):
    pass


class School:
    def __init__(self, students):
        self.students = []

    def add_student(self, students):
        self.students.append(student1, student2, student3, student4, student5)

    def get_best_student(self):
        best_students = []
        for greats in self.students:
            if self.great == 5 or self.great == 6:
                return best_students

    def get_students(self, group_number):
        group_students = []
        if Student.group_number == self.students.group.name:
            group_students.append()
        return group_students

    def get_students_without_exams(self):
        self.astudents.append(Student())

    def avg_maths(self):
        return sum(student.maths for student in self.students) / len(self.students)


student1 = Student('Ivan', 'Ivanov', 15, [4, 7, 8, 5, 4])
student2 = Student('Bill', 'Jonas', 13, [9, 9, 8, 8, 8])
student3 = Student('Nick', 'Jordan', 10, [6, 8, 9, 6, 4])
student4 = Student('Maria', 'Shpak', 13, [7, 9, 8, 7, 7])
student5 = Student('James', 'Cotlin', 15, [6, 7, 8, 9, 9])

school = School()
school.add_student()
print(School.students)
print(School.avg_maths)
