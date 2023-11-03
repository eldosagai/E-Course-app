class Diary:
    def __init__(self, owner, school):
        self.owner = owner
        self.school = school

    def name1(self):
        return self.owner

class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher


    def name1(self):
        return self.teacher

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def display_info(self):
        return f'{self.name} is {self.age} years old'

class Student(Person):
    def __init__(self, name, age, diary, subject):
        super().__init__(name, age)
        self.diary = diary
        self.subject = subject


    def student_diary_info(self):
        return f"{self.name}'s diary is from {self.diary.school}, owned by {self.diary.owner}"


    def student_subject_info(self):
        return f"{self.name}'s subject is {self.subject.name} taught by {self.subject.teacher}"
diary = Diary("Tamarov", "Olymp")
subject = Subject("Math", "Kekova")
student = Student("Arsen", 18, diary, subject)
print(student.display_info())
print(student.student_diary_info())
print(student.student_subject_info())
