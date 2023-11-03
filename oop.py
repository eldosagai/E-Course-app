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
    

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def age_student(self):
        return f'{self.name} is {self.age} years old'    
    
        
diary = Diary("Tamarov", "Olymp")
print(diary.name1())
subject = Subject("Math", "Kekova")
print(subject.name1())
student = Student("Arsen", 18)
print(student.age_student())
