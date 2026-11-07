import os

abeceda = "abcdefghijklmnopqrstuvwxyz"

def sifrovat (text, n):
    sifrovaneSlovo = ""
    for char in text.lower():
        if char.isalpha():
            stara_pozice = abeceda.find(char)
            nova_pozice = (stara_pozice + n) %26
            sifrovaneSlovo += abeceda[nova_pozice]
        else:
            sifrovaneSlovo += char
    return sifrovaneSlovo

def desifrovat (text, n):
    desifrovaneSlovo = ""
    for char in text.lower():
        if char.isalpha():
            stara_pozice = abeceda.find(char)
            nova_pozice = (stara_pozice - n) %26
            desifrovaneSlovo += abeceda[nova_pozice]
        else:
            desifrovaneSlovo += char
    return desifrovaneSlovo

def clearConsole():
    os.system('cls')

def MainMenu():
    print("- - - Cézarova šifra - - -")
    print("(1) Šifrování")
    print("(2) Dešifrování")
    print("(3) Konec")
        
while True:
    MainMenu()
    vstupMain = input("Zadejte volbu: ")
    match (vstupMain):
        case "1":
           vstupSlovo = input("Zadejte text: ")
           vstupPosun = int(input("Zadejte klíč posunu: "))
           print(sifrovat(vstupSlovo,vstupPosun))
        case "2":
           vstupSlovo = input("Zadejte text: ")
           vstupPosun = int(input("Zadejte klíč posunu: "))
           print(desifrovat(vstupSlovo,vstupPosun))
        case "3":
            print("Program se ukončil.")
            exit()
        case _:
            print("Neplatný vstup!")
    input("Stisknete ENTER")       
    clearConsole()