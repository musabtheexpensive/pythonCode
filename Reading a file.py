file=open("student.txt", "r")
print(file.readable())
file.close()

#another programme
file=open("student.txt", "w")
print(file.readable())
file.close()

#another 1 programme
file=open("student.txt", "r+")
text=file.read()
print(text)
size = len(text)
print(size)
file.close()

#another different programme
file=open("student.txt", "r+")
for line in file:
    print(line)
file.close()

#another programme
file = open("student.txt", "r+")
text=file.readlines()[1]
print(text)
file.close()
