origin = []
bob = input("Enter a palindrome: ")

for i in bob:
    if i == ' ':
        pass
    else:
        origin.append(i)

boblower = bob.lower()
boblist = []
boblist.extend(boblower)
boblist.reverse()
bobrev = []

for i in boblist:
    if i == ' ':
        pass
    else:
        bobrev.append(i)

seperator = ""
bobrevcomb = (seperator.join(bobrev))
boblistcomb = (seperator.join(origin))

if boblistcomb == bobrevcomb:
    print(bob, "is a palindrome.")
else:
    print(bob, "is not a palindrome.")
