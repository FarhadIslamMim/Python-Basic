number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result=[x*x for x in number]     #[expression for item in list] for map funcation
print(result)
result=[x for x in number if x%2==0 ]        #for filter function
print(result)