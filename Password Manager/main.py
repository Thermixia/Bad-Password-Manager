import random
import string
import json
import os

def writeStart(type):
    char = int(input("Char#"))

    if type in ("yes", "y"):
        numletgen(char)
    if type in ("no", "n"):
        letgen(char)
    if type not in ("yes", "y", "no", "n"):
        print("Invalid response, assuming yes")
        numletgen(char)

def numletgen(number):
    password = ""
    number = number / 2
    if number is not int(number):
        number = round(number)
        print("due to limitations on my code your number of characters will be " + str(number))

    while number > 0:
        password = password + random.choice(string.ascii_letters)
        password = password + str(random.randint(0,9))
        number -= 1
    helper(password)

def letgen(number):
    password = ""
    while number > 0:
        password = password + random.choice(string.ascii_letters)
        number -= 1
    helper(password)

def helper(password):
    storage = input("Store password? ")
    if storage in ("yes", "y"):
        Website = input("Website: ")
        Username = input("Username: ")
        Password = password
        write(Website, Username, Password)
    if storage in ("no", "n"):
        print(password)
    else:
        helper(password)

def write(Website, Username, Password):
    filename = Website + " as " + Username + ".json"
    obj = {u"Website": Website, u"Username": Username, u"Password": Password}
    obj_storage = json.dumps(obj, indent=4)
    print(obj_storage)
    with open(filename, "w") as file:
        json.dump(obj, file, indent=4)
    quit()

def read():
    Website = input("Website: ")
    Username = input("Username: ")
    filename = Website + " as " + Username + ".json"

    with open(filename, "r") as file:
        data = json.load(file)
    print(data)
