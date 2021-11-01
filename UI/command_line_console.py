from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect
from Domain.obiect import toString

def showAll(lista):
    for obiect in lista:
        print(toString(obiect))


def main_line(lista):
    while True:
        given_string = input()
        if given_string == "help":
            print("add,id,nume,descriere,pret, locatie -> adauga obiectul")
            print("update,id,nume,descriere,pret, locatie -> modifica obiectul")
            print("delete,id -> sterge obiectul")
            print("showall -> afiseaza obiectele din lista")
            print("stop -> oprire program")
        else:
            optiuni = given_string.split(";")
            if optiuni[0] == "stop":
                break;
            else:
                for optiune in optiuni:
                    elemente = optiune.split(",")
                    if(elemente[0] == "add"):
                        try:
                         lista = adauga_obiect(elemente[1], elemente[2], elemente[3], elemente[4], elemente[5],lista)
                        except ValueError as ve:
                         print("Eroare: {}".format(ve))
                    elif elemente[0] == "showall" :
                        showAll(lista)
                    elif elemente[0] == "update" :
                        lista = modifica_obiect(elemente[1], elemente[2], elemente[3], elemente[4], elemente[5],lista)
                    elif elemente[0] == "delete":
                        lista = sterge_obiect(elemente[1], lista)
                    else:
                        print("optine gresita, scrieti 'help' pt a afisa optiunile disponibile ")
