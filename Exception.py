num2=int(input("Enter a number:"))
result = 20/num2
print(result)
print("Done")

#another programme
text="Musab"
print(text[4])
print("Done")

#another programme
try:
    list=[20,0,30]
    result=list[0] / list[4]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing by zero is not possible")
except IndexError:
    print("Index error")
    print("successfull")