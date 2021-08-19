numberofword = 0
numberofdiget = 0
numberofletter = 0


n = input("Enter a text of number:")

for x in n:
    x = x.lower()
    if x >= "a" and x <= "z":
        numberofletter = numberofletter + 1
    elif x >= "0" and x <= "9":
        numberofdiget = numberofdiget + 1
    elif x == " " :
        numberofword = numberofword + 1

print("words:",numberofword+1)
print("Digit:",numberofdiget)
print("Letter:",numberofletter)


