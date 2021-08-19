from random import randint
for i in range(1,7):
    x=input("Enter a Number Between(1-6):")
    randomnumber=randint(1,6)
    if randomnumber==x:
       print("You Won!")
    else:
      print("you loss!")
      print("Random number was:",randomnumber)