# BaklyshaOS_Installer.py
import os
import time

user = os.getlogin()

print("BaklyshaOS")
print("---------------------------")
print("1. Install BaklyshaOS")
print("2. Boot existing os")
print("---------------------------")

def ccc():
    os.system("cls")
    print("Write path to launch file")
    cc = input("* ")
    try:
        os.startfile(cc)
        print("Finish! This window will be closed in 5 seconds")
        time.sleep(5)
    except Exception as e:
        print(f"E : {e}")
        ccc()

def ccccc():
    os.system("cls")
    print("You have git?(Check this in cmd, write 'git --version', if in output error - you not have git. Y/N)")
    cccc = input("Y/N")
    if cccc == "N":
        print("Go to https://gitforwindows.org/ and install it")
        time.sleep(15)
        ccccc()
    elif cccc == "Y":
        print("Ok, installation...")
        os.system("git clone ")
        print("Finish! This window will be closed in 5 seconds")
        time.sleep(5)
    else:
        print("Unknown choose...")
        time.sleep(5)
        ccccc()
    print("Finish! This window will be closed in 5 seconds")
    time.sleep(5)

def c():
    c = input("* ")
    if c == "1":
        ccccc()
    elif c == "2":
        ccc()
    else:
        os.system("cls")
        print("Unknown choose...")
        time.sleep(5)
        os.system("cls")
        c()

c()
