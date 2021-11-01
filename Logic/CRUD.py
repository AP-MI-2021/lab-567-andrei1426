from Domain.obiect import creeaza_obiect, get_id


def adauga_obiect(id, nume, descriere, pret, locatie, lista):
    '''
    adauga o prajitura intr-o lista
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :param lista: lista de obiecte
    :return: o lista continand atat elementele vechi, cat si noul obiect
    '''
    obiect = creeaza_obiect(id, nume, descriere, pret, locatie)
    return lista + [obiect]


def get_by_id(id, lista):
    '''
    gaseste un obiect cu id-ul dat intr-o lista
    :param id: string
    :param lista: lista de obiecte
    :return: obiectul cu id-ul dat din lista sau None, daca acesta nu exista
    '''
    for obiect in lista:
        if get_id(obiect) == id:
            return obiect
    return None


def sterge_obiect(id, lista):
    """
    sterge un obiect cu id-ul dat din lista
    :param id: id-ul obiectului care se va sterge
    :param lista: lista de obiecte
    :return: o lista de obiecte fara elementul cu id-ul dat
    """
    return [obiect for obiect in lista if get_id(obiect) != id]


def modifica_obiect(id, nume, descriere, pret, locatie, lista):
    """
    modifica un obiect cu id-ul dat
    :param id: id-ul obiectului
    :param nume: numele obiectului
    :param descriere: descrierea obiectului
    :param pret: pretul obiectului
    :param locatie: locatia obiectului
    :param lista: O lista de obiecte.
    :return: lista modificata.
    """
    lista_noua = []
    for obiect in lista:
        if get_id(obiect) == id:
            obiect_nou = creeaza_obiect(id, nume, descriere, pret, locatie)
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua