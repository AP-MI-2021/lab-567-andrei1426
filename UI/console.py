from Domain.obiect import toString
from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect
from Logic.functionalitate import schimbare_locatie, schimbare_descriere_dupa_pret,max_pret_fiecare_locatie,sum_pret_fiecare_locatie,sortare_dupa_pret

def printMenu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("4. Mutarea obiectelor dintr-o locatie in alta")
    print("5.  Concatenarea unui string citit la toate descrierile "
         "obiectelor cu prețul mai mare decât o valoare citită")
    print("6.Determinarea celui mai mare preț pentru fiecare locație")
    print("7.Ordonarea obiectelor crescător după prețul de achiziție")
    print("8.Determinarea suma preturilor pentru fiecare locație")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare obiecte")
    print("x. Iesire")


def ui_adauga_obiect(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        descriere = input("Dati descrierea: ")
        pret = float(input('Dati pretul: '))
        locatie = input("Dati locatia: ")
        rezultat = adauga_obiect(id, nume, descriere, pret, locatie, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def ui_sterge_obiect(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul obiectului de sters: ")

        rezultat = sterge_obiect(id, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_modifica_obiect(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul obiectului de modificat: ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret = float(input('Dati noul pret: '))
        locatie = input("Dati noua locatie: ")

        rezultat = modifica_obiect(id, nume, descriere, pret, locatie, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_max_pret_fiecare_locatie(lista):
    rezultat=max_pret_fiecare_locatie(lista)
    for locatie in rezultat:
        print("Locatia {} are pretul maxim {}".format(locatie, rezultat[locatie]))


def ui_sortare_dupa_pret(lista):
    showAll(sortare_dupa_pret(lista))


def ui_sum_pret_fiecare_locatie(lista):
    rezultat=sum_pret_fiecare_locatie(lista)
    for locatie in rezultat:
        print("Locatia {} are suma preturilor {}".format(locatie, rezultat[locatie]))


def showAll(lista):
    for obiect in lista:
        print(toString(obiect))


def run_menu(lista):
    undo_list = []
    redo_list = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = ui_adauga_obiect(lista, undo_list, redo_list)
        elif optiune == "2":
            lista = ui_sterge_obiect(lista, undo_list, redo_list)
        elif optiune == "3":
            lista = ui_modifica_obiect(lista, undo_list, redo_list)
        elif optiune == "4":
            undo_list.append(lista)
            redo_list.clear()
            locatie_initiala = input("din ce locatie doresti sa le muti? ")
            locatie_noua = input("in ce locatie doresti sa se afle obiectele? ")
            lista = schimbare_locatie(locatie_initiala, locatie_noua,lista)
        elif optiune == "5":
            undo_list.append(lista)
            redo_list.clear()
            str_concat=input("ce string doresti sa adaugi? ")
            pret_comparat=int(input("cu ce valoare doresti sa compari preturile? "))
            lista=schimbare_descriere_dupa_pret(pret_comparat,str_concat,lista)
        elif optiune == "6":
            ui_max_pret_fiecare_locatie(lista)
        elif optiune == "7":
            ui_sortare_dupa_pret(lista)
        elif optiune == "8":
            ui_sum_pret_fiecare_locatie(lista)
        elif optiune == "u":
            if len(undo_list) > 0:
                redo_list.append(lista)
                lista = undo_list.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redo_list) > 0:
                undo_list.append(lista)
                lista = redo_list.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")

