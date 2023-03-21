#parent class=super class=Base class
#child class=sub class=Derived class
class phone:
    def call(self):
        print("You can call")

    def message(self):
        print("You can Message")


class Samsung(phone):
      #call,message
    def photo(self):
        print("You can take photo")
'''
    def message(self):
        print("You can Message")
    def photo(self):
        print("You can take photo")
'''
#p = phone()
#p.message()
#p.call()
s = Samsung()
s.message()
s.call()
s.photo()


#amra chacci j samsung class ti phone class er sub class kina tahole
print(issubclass(Samsung,phone))
print(issubclass(phone,Samsung))