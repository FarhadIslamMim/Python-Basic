"""num1 = 34
num2 = 5
num3 = 90
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)"""

char = input("Enter a char.:")
num = int(input("Enter a number"))
if 50 <= num <= 100:
    print("number is between 50 and 100")
else:
    print("not in range")
if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" \
        or char == "I" or char == "O" or char == "U":
    print(char+" is vowel")
else:
    print(char+" is Consonant")