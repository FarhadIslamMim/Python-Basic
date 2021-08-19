try:
    num1=int(input("Enter a Number:"))
    num2=int(input("Enter a Number2:"))
    result=num1/num2
    print(result)
    print("done")
except (ZeroDivisionError,ValueError):
    print("you have enter wrong input")

finally:
    print("Success")