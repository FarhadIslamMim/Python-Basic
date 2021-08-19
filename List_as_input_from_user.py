#10 20 30
n= input("Enter a text of number:")
#10,20,30...
list=n.split()
sum=0
for x in list:
    sum=sum+int(x)
print(list)
print(sum)
