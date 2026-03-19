import json

print("Booting...")
while True:
    cmd = input("Insert your command: ")
    if cmd == "/list":
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                print(f"Your list: {data}")
        except Exception:
            print("List is empty.")

    elif cmd == "/add":
        with open("data.json", "a") as f:
            while True:
                userinput = input("Insert your data or '/done': ")
                if userinput == "/done":
                    break
                else:
                    f.write(userinput)
    elif cmd == "/clear":
        with open("data.json", "w"):
            None
        print("cleared.")

    elif cmd == "/stop":
        print()
        break
    elif cmd == "/help":
        print("/list - list data, /add - add data, /stop - close program\n/clear - clear list, /help - ask for help")

    else:
        print("CMD not in list")
