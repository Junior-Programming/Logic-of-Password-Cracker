from random import *

userPass = input("\nEnter your password:")

password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', ]

guessPass = ""

while (guessPass != userPass):
    guessPass = ""
    for letter in range(len(userPass)):
        guessLetter = password[randint(0, 25)]
        guessPass = str(guessLetter) + str(guessPass)
    print(guessPass)

print("Result marched password is: ", guessPass)
