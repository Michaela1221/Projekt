from pojistenci import Pojistenci
from nazev import Nazev

uvod = Nazev()

def print_menu():
    print(uvod)
    print("Vyberte si akci: ")
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojistného")
    print("4 - Konec")
    return int(input(""))



pojistenci = Pojistenci()


while True:
    vyber = print_menu()
    if (vyber == 1):
        pojistenci.pridat_pojistence()
    elif (vyber == 2):
        pojistenci.vypsat_pojistence()
    elif (vyber == 3):
        pojistenci.vyhledat()
    elif (vyber == 4):
        print("Konec")
        break
    else:
        print()
        print("Zadali jste špatné číslo, zkuste to prosím znovu ")


