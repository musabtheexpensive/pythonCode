num1= {1,2,3,4,5,6,7,87,}
print(num1)
num2= set([4,5,6])
print(num2)
num2.add(7)
print(num2)
num2.remove(5)
print(num2)
print(8 in num2)
print(9 not in num2)

# Set er Ashol Bebohar .... ,,. ,,

num3= {1,2,3,4,5,6,7,8,}
num4= set([4,5,6,7])

print(num3 |  num4)
print(num3 &  num4)
print(num3 -  num4)