import main

action = input("Read or Write?").lower()
if action not in ("read", "write"):
    print("Error, assuming read")
    main.read()
if action == "read":
    main.read()
if action == "write":
    numbers = str(input("Numbers?"))
    main.writeStart(numbers)
