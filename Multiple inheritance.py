class A:
    def display(self):
        print("I am inside A class")

class B:
    def display(self):
        print("I am inside B class")

class C(A,B):
    '''
    def display(self):
        print("I am inside C class")
    '''

ob1=C()
ob1.display()