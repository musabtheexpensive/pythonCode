

# suppose amra chacci j user er kac theke j input ta nibo shetar mott word,letter,digit jante chacci taile nicher programme

numOfWords=0
numOfLetters=0
numOfDigits=0

text=input("Enter a text of numbers: ")

for x in text:
    x=x.lower()
    if x >='a' and x <='z':
        numOfLetters=numOfLetters+1
    elif x >='0' and x <='9':
        numOfDigits=numOfDigits+1
    elif x == ' ':
        numOfWords=numOfWords+1

print("Number of Letters :",numOfLetters)
print("Number of Digits :",numOfDigits)
print("Number of Words :",numOfWords)
