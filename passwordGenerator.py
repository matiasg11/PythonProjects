#Do you want to generate a random password?
#Ask for length
#Generate password
#Print Password
#Exit and goodbye

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%&*()+.-")

def genPass():
    passLength = int(input("What's the length of the password? "))
    random.shuffle(characters)
    password = []
    for i in range(passLength):
        password.append(random.choice(characters)) 

    random.shuffle(password)

    print("".join(password))

option = input("Do you want a new password? Y/N  ")

if option == "Y" or option == "y":
    genPass()
elif option == "N":
    print("Goodbye")
    quit()
else:
    print("Wrong answer, goodbye")
    quit()