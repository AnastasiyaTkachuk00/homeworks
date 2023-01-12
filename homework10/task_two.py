class ValidationError(Exception):
    pass


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


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
    
    def get_best_students(self):
        best_students = []
        for student in self.students:
            great_set = set(student.great)
        if not great_set.intersection({1, 2, 3, 4, 7, 8, 9, 10}):
            best_students.append(student)
            return best_students

    def get_students(self, group_number):
        group_students = []
        for group_number in self.students:
            if group_number in school.students:
                group_students.append()
            return group_students
    
    def get_students_without_exams(self):
        return sum(student.great for student in self.students) / len(self.students)


school = School()
school.add_student(Student('Bill', 'Jonas', 13, [9, 9, 8, 8, 8]))
school.add_student(Student('Nick', 'Jordan', 10, [6, 8, 9, 6, 4]))
school.add_student(Student('Maria', 'Shpak', 13, [7, 9, 8, 7, 7]))
school.add_student(Student('James', 'Cotlin', 15, [6, 7, 8, 9, 9]))
print(school.students)
