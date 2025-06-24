import os

current_user = "User"

print("Hi from BaklyshaOS!")
def cc():
    global current_user
    command = c
    two = command.split()
    if command == "clear":
        os.system("cls")
    elif command == "hi":
        print("Hi!")
    elif command == "root":
        print("Hey, root-access this is not a joke, you can do harm to you device")
        ccc = input("You sure??(Y/N) ")
        if ccc == "Y":
            current_user = "Root"
            print("Ok, be careful, for exit from root access write user")
        elif ccc == "N":
            print("Ok")
        else:
            print("Unknown choose")
    elif command == "user":
        current_user == "User"
        print("Succes")
    elif command == "rm":
        rrr = input("PATH : ")
        if current_user == "User":
            print("Access denied, please write 'root'")
        elif current_user == "Root":
            g = input(f"You sure remove file or directory '{rrr}'(Y/N) ")
            if g == "Y":
                try:
                    os.remove(rrr)
                    print("Succes")
                except Exception as e:
                    print(f"E : {e}")
            elif g == "N":
                print("Ok")
            else:
                print("Unknown choose...")
    else:
        print("Unknown command...")
    return current_user

while True:
    c = input(f"BaklyshaOS@{current_user}> ")
    cc()
