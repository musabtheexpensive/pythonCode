class Student:
    roll=""
    gpa=""

    def set_Value(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")

rahim=Student()
rahim.set_Value(123,4.12)
rahim.display()


karim=Student()
karim.set_Value(543,4.99)
karim.display()