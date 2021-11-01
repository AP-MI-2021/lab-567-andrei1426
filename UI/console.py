from Domain.obiect import toString
from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect
from Logic.functionalitate import schimbare_locatie, schimbare_descriere_dupa_pret

def printMenu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("4. Mutarea obiectelor dintr-o locatie in alta")
    print("5.  Concatenarea unui string citit la toate descrierile "
         "obiectelor cu prețul mai mare decât o valoare citită.")
    print("a. Afisare prajituri")
    print("x. Iesire")


def ui_adauga_obiect(lista):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        descriere = input("Dati descrierea: ")
        pret = float(input('Dati pretul: '))
        locatie = input("Dati locatia: ")
        return adauga_obiect(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def ui_sterge_obiect(lista):
    id = input("Dati id-ul obiectului de sters: ")
    return sterge_obiect(id, lista)


def ui_modifica_obiect(lista):
    id = input("Dati id-ul obiectului de modificat: ")
    nume = input("Dati noul nume: ")
    descriere = input("Dati noua descriere: ")
    pret = float(input('Dati noul pret: '))
    locatie = input("Dati noua locatie: ")
    return modifica_obiect(id, nume, descriere, pret, locatie, lista)


def showAll(lista):
    for obiect in lista:
        print(toString(obiect))


def run_menu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = ui_adauga_obiect(lista)
        elif optiune == "2":
            lista = ui_sterge_obiect(lista)
        elif optiune == "3":
            lista = ui_modifica_obiect(lista)
        elif optiune == "4":
            locatie_initiala = input("din ce locatie doresti sa le muti? ")
            locatie_noua = input("in ce locatie doresti sa se afle obiectele? ")
            lista = schimbare_locatie(locatie_initiala, locatie_noua,lista)
        elif optiune == "5":
            str_concat=input("ce string doresti sa adaugi? ")
            pret_comparat=int(input("cu ce valoare doresti sa compari preturile? "))
            lista=schimbare_descriere_dupa_pret(pret_comparat,str_concat,lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")