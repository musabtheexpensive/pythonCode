class phone:
    def __init__(self):
        print("I am in phone class")

class Samsung(phone):
    #init
    pass

s = Samsung()

#another programme of overriding

class phone:
    def __init__(self):
        print("I am in   class")

class Samsung(phone):
    #init
    def __init__(self):
        super().__init__()
        print(("I Am Your Boss"))

s = Samsung()

