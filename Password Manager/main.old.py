import random
import string
import json

def write():
    number = int(input("Char#: "))
    digi = input("Numbers? ")
    password = ""
    digipass = ""

    if digi in ("yes", "y"):
        diginumber = number / 2
        number = number / 2
        while diginumber > 0:
            digipass = digipass + str(random.randint(0,10))

    while number > 0:
        password = password + random.choice(string.ascii_letters)
        number -= 1

    if digi in ("yes", "y"):
        password = password + digipass

    if number == 0:
        print(password)

        store = input("Store Password? ").lower()

        if store not in ("yes", "y", "no", "n"):
            print("Error, assuming yes")
            information(password)

        if store in ("yes", "y"):
            information(password)

        if store in ("no", "n"):
            print("Not stored")

def information(Password):
    Username = input("Username: ")
    Website = input("For: ")
    store(Website, Username, Password)

def store(Website, Username, Password):
    obj = {u"Website": Website, u"Username": Username, u"Password": Password}
    obj_storage = json.dumps(obj, indent=4)
    print(obj_storage)
    with open(Website, "w") as file:
        json.dump(obj, file, indent=4)

def read():
    Website = input("Website: ")

    with open(Website, "r") as file:
        data = json.load(file)
    print(data)
