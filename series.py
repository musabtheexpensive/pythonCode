#2+4+6+8+10+....+n
n= int (input("Enter the last number :"))
sum=0
for x in range(2,n+1,2):
    sum=sum+x
    print(sum)

#notunvabe shuru hobe onno programme
#1+2+3+4+5+....+n
n= int (input("Enter the last number :"))
sum=0
for x in range(1,n+1,1):
    sum=sum+x
    print(sum)

#notunvabe shuru hobe onno programme
#1*1+2*2+3*3+....+n*n

n= int (input("Enter the last number :"))
sum=0
for x in range(1,n+1,1):
    sum=sum+x*x
    print(sum)

#notunvabe shuru hobe onno programme
#1x2x3x....xn
n= int (input("Enter the last number :"))
sum=1
for x in range(1,n+1,1):
    sum=sum*x
    print(sum)