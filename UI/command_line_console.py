from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect
from Domain.obiect import toString

def showAll(lista):
    for obiect in lista:
        print(toString(obiect))


def main_line(lista):
    undo_list = []
    redo_list = []
    while True:
        given_string = input()
        if given_string == "help":
            print("add,id,nume,descriere,pret, locatie -> adauga obiectul")
            print("update,id,nume,descriere,pret, locatie -> modifica obiectul")
            print("delete,id -> sterge obiectul")
            print("showall -> afiseaza obiectele din lista")
            print("undo -> undo")
            print("redo -> redo")
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
                             undo_list.append(lista)
                             redo_list.clear()
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                    elif elemente[0] == "showall" :
                        showAll(lista)
                    elif elemente[0] == "update" :
                        try:
                            lista = modifica_obiect(elemente[1], elemente[2], elemente[3], elemente[4], elemente[5],lista)
                            undo_list.append(lista)
                            redo_list.clear()
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))

                    elif elemente[0] == "delete":
                        try:
                            lista = sterge_obiect(elemente[1], lista)
                            undo_list.append(lista)
                            redo_list.clear()
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                    elif elemente[0] == "undo":
                        if len(undo_list) > 0:
                            redo_list.append(lista)
                            lista = undo_list.pop()
                        else:
                            print("Nu se poate face undo!")
                    elif elemente[0] == "redo":
                        if len(redo_list) > 0:
                            undo_list.append(lista)
                            lista = redo_list.pop()
                        else:
                            print("Nu se poate face redo!")
                    else:
                        print("optine gresita, scrieti 'help' pt a afisa optiunile disponibile ")
