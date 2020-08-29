from os import system, name

def cls():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")