"""
1.start
2.input guessNumber
3.Generate random number
4.if guess Number==random number
     i) yes,print won
     ii) No, print Lost
5.End
"""
from random import randint

for x in range(1):
  guessNumber=int(input("Enter your guess number between 1 to 8 :"))
  randomNumber=randint(1,8)

  if guessNumber== randomNumber:
      print("You Have Won")
  else:
      print("You Have lost")
      print("Random number was:",randomNumber)



