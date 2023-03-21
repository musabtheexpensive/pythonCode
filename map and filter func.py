#map function
def square(x):
    return x*x
num= [1,2,3,4,5]
result = list(map(square,num))
print(result)

# filter function
num= [1,2,3,4,5]

result= list(filter(lambda x: x%2==0,num))
result=[x for x in num if x%2==0]
print(result)
