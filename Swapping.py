"""a=20
b=30
temp=a
a=b
b=temp
print(a,b)"""

"""a=20
b=30
a=a+b    #a=20+30=50
b=a-b    #b=50-30=20
a=a-b    #a=50-20=30
print(a,b)"""
#IN PYTHON

a=20
b=30
a,b=b,a
print("a=",a)
print("b=",b)