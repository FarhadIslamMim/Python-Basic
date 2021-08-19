#xxarg
"""def student(*detaisl):
    print(detaisl)
student(101, "mim", 3.30)
student(102, "fahim", 3.50)
student(103, "rahim", 4.00)
"""
def add(*numbers):
    sum=0
    for x in numbers:
        sum=sum+x
        return sum
#add(12)
print(add(12,13))
#add(12,13,14)
#add(12,13,14,15)