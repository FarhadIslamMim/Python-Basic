file=open("student.txt","r+")
#print(file.writable())
text=file.read()
print(text)
#text=file.readlines()[3]
#print(text)
#for x in file:
    #print(x)
file.close()