try:
    num1=int(input("Enter The First Number"))
    num2=int(input("Enter The secound number"))
    result=num1/num2
    print(result)
except (ValueError,ZeroDivisionError):
    print('you have entered incorrect input...')


finally:
    print("Thanks A Lot little Brother")

#another programem
def voter (age):
    if age<18:
        raise ValueError("Invaild Voter")
    return " You are allowed to vote"
try:

    print(voter(17))
except ValueError as e:
    print(e)
