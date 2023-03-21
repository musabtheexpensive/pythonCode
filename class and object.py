class Student:
    roll=""
    gpa=""



rahim = Student()
print(isinstance(rahim,Student))

rahim.roll=101
rahim.gpa=3.85
print(f"Roll : {rahim.roll}, GPA : {rahim.gpa}")

Karim = Student()
Karim.roll=101
Karim.gpa=3.96
print(f"Roll : {Karim.roll}, GPA : {Karim.gpa}")