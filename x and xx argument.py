#xargs
def student(id,name):
    print(id,name)

student(101,"Musab")

#01 right programme
def student(*details):
    print(details)

student(212,"Musab VAi")
student(223,"Mahi",5.00)

# x argument er sahajje  2 ti ba 3ti shonkhar jogfolll
def add (*numbers):
    sum=0
    for num in numbers:
     sum=sum+num
    print(sum)

add(10,20)
add(10,20,30)
add(10,20,30,40)

#xxargument programme
def student(**details):
    print(details["name"])

student(id=101,name="Musab")